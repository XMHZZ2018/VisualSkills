"""
Trajectory Viewer — Streamlit app for comparing agent runs across skill modes.

Data lives on the remote VM; this app fetches on demand via gcloud SSH.

Usage:
    streamlit run scripts/trajectory_viewer.py
"""
import base64
import json
import os
import subprocess
from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
VM_NAME = os.environ.get("VM_NAME", "osworld")
VM_ZONE = os.environ.get("VM_ZONE", "us-west1-c")
WORKSPACE_ROOT = "/home/ziyan/MMSkills/scripts/run-gym-anything/workspaces"

SKILL_MODES = ["skill-none", "skill-text", "skill-multimodal"]
SKILL_LABELS = {
    "skill-none": "No Skill",
    "skill-text": "Text Skill",
    "skill-multimodal": "Multimodal Skill",
}
MODE_COLORS = {
    "skill-none": "#ff6b6b",
    "skill-text": "#4ecdc4",
    "skill-multimodal": "#45b7d1",
}


# ---------------------------------------------------------------------------
# Remote helpers
# ---------------------------------------------------------------------------
@st.cache_data(ttl=300)
def ssh_run(cmd: str) -> str:
    full = f'gcloud compute ssh {VM_NAME} --zone={VM_ZONE} -- "{cmd}"'
    result = subprocess.run(full, shell=True, capture_output=True, text=True, timeout=30)
    return result.stdout.strip()


@st.cache_data(ttl=300)
def ssh_read_file(path: str) -> str:
    return ssh_run(f"cat {path}")


@st.cache_data(ttl=600)
def ssh_read_image(path: str) -> bytes:
    full = f"gcloud compute ssh {VM_NAME} --zone={VM_ZONE} -- 'base64 {path}'"
    result = subprocess.run(full, shell=True, capture_output=True, text=True, timeout=30)
    return base64.b64decode(result.stdout.strip())


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
@st.cache_data(ttl=120)
def list_experiments() -> list[str]:
    out = ssh_run(f"ls {WORKSPACE_ROOT}")
    return sorted(out.split()) if out else []


@st.cache_data(ttl=120)
def list_available_modes(exp: str) -> list[str]:
    out = ssh_run(f"ls {WORKSPACE_ROOT}/{exp}")
    dirs = out.split() if out else []
    return [d for d in SKILL_MODES if d in dirs]


@st.cache_data(ttl=120)
def list_softwares(exp: str, mode: str) -> list[str]:
    out = ssh_run(f"ls {WORKSPACE_ROOT}/{exp}/{mode}")
    return sorted(out.split()) if out else []


@st.cache_data(ttl=120)
def list_tasks(exp: str, mode: str, software: str) -> list[str]:
    out = ssh_run(f"ls {WORKSPACE_ROOT}/{exp}/{mode}/{software}")
    return sorted(out.split()) if out else []


@st.cache_data(ttl=120)
def list_screenshots(exp: str, mode: str, software: str, task: str) -> list[str]:
    path = f"{WORKSPACE_ROOT}/{exp}/{mode}/{software}/{task}/screenshots"
    out = ssh_run(f"ls {path} 2>/dev/null")
    if not out:
        return []
    return sorted([f for f in out.split() if f.endswith(".png")])


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
@st.cache_data(ttl=300)
def load_result(exp: str, mode: str, software: str, task: str) -> dict:
    path = f"{WORKSPACE_ROOT}/{exp}/{mode}/{software}/{task}/result.json"
    text = ssh_read_file(path)
    try:
        return json.loads(text)
    except (json.JSONDecodeError, ValueError):
        return {"error": f"Could not parse: {text[:200]}"}


@st.cache_data(ttl=600)
def load_task_json(software: str, task: str) -> dict:
    """Load task.json from the gym-anything tasks directory on the VM."""
    ga_tasks = (
        "/home/ziyan/MMSkills/vendor/gym-anything/benchmarks/cua_world"
        f"/environments/{software}/tasks/{task}/task.json"
    )
    text = ssh_read_file(ga_tasks)
    try:
        return json.loads(text)
    except (json.JSONDecodeError, ValueError):
        return {}


@st.cache_data(ttl=300)
def load_prompt(exp: str, mode: str, software: str, task: str) -> str:
    path = f"{WORKSPACE_ROOT}/{exp}/{mode}/{software}/{task}/prompt.txt"
    return ssh_read_file(path)


MCP_PREFIX = "mcp__gym-anything-controller__"
# Tools that are internal to Claude CLI, not GUI actions
SKIP_TOOLS = {"ToolSearch"}
# Tools that represent skill/file reading, not GUI actions
SKILL_TOOLS = {"Read", "Glob", "Grep"}


def _format_action(tool_name: str, tool_input: dict) -> tuple[str, str]:
    """Return (short_name, detail) for a tool call."""
    short = tool_name.replace(MCP_PREFIX, "")
    detail = ""
    if short in ("click", "double_click"):
        detail = f"({tool_input.get('x', '?')}, {tool_input.get('y', '?')})"
    elif short == "type_text":
        t = tool_input.get("text", "")
        detail = repr(t[:80]) + ("..." if len(t) > 80 else "")
    elif short == "key_press":
        detail = str(tool_input.get("key", ""))
    elif short == "hotkey":
        detail = str(tool_input.get("keys", ""))
    elif short == "scroll":
        detail = f"({tool_input.get('x', '?')}, {tool_input.get('y', '?')}, clicks={tool_input.get('clicks', '?')})"
    elif short == "drag_to":
        detail = f"({tool_input.get('start_x', '?')},{tool_input.get('start_y', '?')}) -> ({tool_input.get('end_x', '?')},{tool_input.get('end_y', '?')})"
    elif short == "Read":
        fp = tool_input.get("file_path", "")
        detail = fp.split("/")[-1] if "/" in fp else fp
    return short, detail


@st.cache_data(ttl=300)
def parse_trajectory(exp: str, mode: str, software: str, task: str) -> list[dict]:
    """Parse claude_output.txt into a list of agent steps.

    Screenshot files are named step_NNN.png where NNN = the overall tool_use
    index (1-based). Only MCP controller tool calls produce screenshot files.
    ToolSearch and Claude CLI tools (Read, Glob) don't produce screenshots.

    We merge consecutive assistant messages (thinking → text → tool_use) into
    one logical step.
    """
    path = f"{WORKSPACE_ROOT}/{exp}/{mode}/{software}/{task}/claude_output.txt"
    raw = ssh_read_file(path)
    if not raw:
        return []

    events = []
    for line in raw.strip().split("\n"):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue

    # First pass: collect all tool_use calls to build the index → screenshot mapping
    # The bridge saves screenshots as step_{tool_use_index}.png for MCP calls only
    tool_use_index = 0
    mcp_call_indices = {}  # tool_use_index → True if MCP call

    for ev in events:
        if ev.get("type") != "assistant":
            continue
        content = ev.get("message", {}).get("content", [])
        if not isinstance(content, list):
            continue
        for block in content:
            if isinstance(block, dict) and block.get("type") == "tool_use":
                tool_use_index += 1
                name = block.get("name", "")
                is_mcp = name.startswith(MCP_PREFIX)
                mcp_call_indices[tool_use_index] = is_mcp

    # Second pass: build steps
    steps = []
    tool_use_counter = 0
    cur_thinking = []
    cur_text = []

    for ev in events:
        ev_type = ev.get("type", "")

        if ev_type == "assistant":
            content = ev.get("message", {}).get("content", [])
            if not isinstance(content, list):
                continue
            for block in content:
                if not isinstance(block, dict):
                    continue
                bt = block.get("type", "")
                if bt == "thinking":
                    cur_thinking.append(block.get("thinking", ""))
                elif bt == "text":
                    cur_text.append(block.get("text", ""))
                elif bt == "tool_use":
                    tool_use_counter += 1
                    name = block.get("name", "")
                    inp = block.get("input", {})

                    # Skip ToolSearch entirely
                    if name in SKIP_TOOLS:
                        continue

                    short, detail = _format_action(name, inp)
                    is_mcp = name.startswith(MCP_PREFIX)

                    # MCP calls have a screenshot file
                    screenshot_file = None
                    if is_mcp:
                        screenshot_file = f"step_{tool_use_counter:03d}.png"

                    # Determine if this is a skill-loading action
                    is_skill_load = name in SKILL_TOOLS

                    steps.append({
                        "thinking": "\n\n".join(t for t in cur_thinking if t),
                        "text": "\n".join(t for t in cur_text if t),
                        "action": short,
                        "action_detail": detail,
                        "action_input": inp,
                        "screenshot_file": screenshot_file,
                        "is_skill_load": is_skill_load,
                        "is_mcp": is_mcp,
                    })
                    cur_thinking = []
                    cur_text = []

    return steps


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------
def render_step(step: dict, step_num: int, exp: str, mode: str, software: str,
                task: str, show_screenshot: bool = True):
    """Render a single step in the trajectory."""
    action = step["action"]
    detail = step["action_detail"]
    is_skill = step.get("is_skill_load", False)

    # Action badge colors
    if is_skill:
        st.markdown(f"**Step {step_num}** — :green[**Skill Load**] `{action}({detail})`")
    else:
        action_colors = {
            "screenshot": "blue",
            "click": "red",
            "double_click": "red",
            "type_text": "green",
            "key_press": "orange",
            "hotkey": "orange",
            "scroll": "violet",
            "drag_to": "violet",
            "move_to": "violet",
        }
        color = action_colors.get(action, "gray")
        st.markdown(f"**Step {step_num}** — :{color}[**{action}**] `{detail}`")

    # Thinking
    if step["thinking"]:
        with st.expander("Thinking", expanded=False):
            st.markdown(step["thinking"][:3000])

    # Text response
    if step["text"]:
        st.caption(step["text"][:500])

    # Screenshot (only for MCP actions)
    if show_screenshot and step.get("screenshot_file"):
        path = f"{WORKSPACE_ROOT}/{exp}/{mode}/{software}/{task}/screenshots/{step['screenshot_file']}"
        try:
            img_bytes = ssh_read_image(path)
            st.image(img_bytes, caption=step["screenshot_file"], use_container_width=True)
        except Exception:
            pass  # screenshot doesn't exist for this step — skip silently


def main():
    st.set_page_config(page_title="MMSkills Trajectory Viewer", layout="wide")
    st.title("MMSkills Trajectory Viewer")

    # Sidebar: selection
    with st.sidebar:
        st.header("Select Run")

        experiments = list_experiments()
        if not experiments:
            st.error("No experiments found on VM. Is the VM running?")
            return
        exp = st.selectbox("Experiment (model)", experiments)

        available_modes = list_available_modes(exp)
        all_softwares = set()
        for m in available_modes:
            all_softwares.update(list_softwares(exp, m))
        all_softwares = sorted(all_softwares)

        if not all_softwares:
            st.warning("No software environments found.")
            return
        software = st.selectbox("Software", all_softwares)

        all_tasks = set()
        mode_task_map = {}
        for m in available_modes:
            tasks = list_tasks(exp, m, software)
            mode_task_map[m] = tasks
            all_tasks.update(tasks)
        all_tasks = sorted(all_tasks)

        if not all_tasks:
            st.warning("No tasks found.")
            return
        task = st.selectbox("Task", all_tasks)

        modes_with_task = [m for m in available_modes if task in mode_task_map.get(m, [])]

        st.divider()
        st.subheader("Compare Modes")
        selected_modes = st.multiselect(
            "Select modes to compare",
            modes_with_task,
            default=modes_with_task,
            format_func=lambda m: SKILL_LABELS.get(m, m),
        )

        st.divider()
        show_screenshots = st.checkbox("Show screenshots", value=True)
        st.caption("Disable to speed up loading")

    if not selected_modes:
        st.info("Select at least one mode to view.")
        return

    # -----------------------------------------------------------------------
    # Task description & evaluation criteria
    # -----------------------------------------------------------------------
    task_json = load_task_json(software, task)
    if task_json:
        st.subheader("Task")
        st.markdown(f"**{task}**" + (f" — `{task_json.get('difficulty', '')}`"
                    if task_json.get("difficulty") else ""))
        st.info(task_json.get("description", "No description available."))

        # Evaluation criteria from metadata
        metadata = task_json.get("metadata", {})
        success = task_json.get("success", {})
        if metadata or success:
            with st.expander("Evaluation Criteria", expanded=True):
                if success:
                    mode_str = success.get("mode", "unknown")
                    spec = success.get("spec", {})
                    st.markdown(f"**Mode:** `{mode_str}`")
                    if spec.get("program"):
                        st.markdown(f"**Verifier:** `{spec['program']}`")
                if metadata:
                    # Show relevant evaluation parameters
                    eval_keys = {k: v for k, v in metadata.items()
                                 if k not in ("target_path",)}
                    if eval_keys:
                        cols_meta = st.columns(min(len(eval_keys), 4))
                        for i, (k, v) in enumerate(eval_keys.items()):
                            label = k.replace("_", " ").title()
                            if isinstance(v, list):
                                cols_meta[i % len(cols_meta)].markdown(
                                    f"**{label}:**\n" + "\n".join(f"- {item}" for item in v))
                            else:
                                cols_meta[i % len(cols_meta)].metric(label, v)

        st.divider()

    # -----------------------------------------------------------------------
    # Header: score summary
    # -----------------------------------------------------------------------
    cols = st.columns(len(selected_modes))
    mode_data = {}
    for col, mode in zip(cols, selected_modes):
        with col:
            result = load_result(exp, mode, software, task)
            steps = parse_trajectory(exp, mode, software, task)
            mode_data[mode] = {"result": result, "steps": steps}

            score = result.get("score", "?")
            elapsed = result.get("elapsed_seconds", "?")
            if isinstance(elapsed, (int, float)):
                elapsed = f"{elapsed:.0f}s"

            color = MODE_COLORS.get(mode, "#666")
            st.markdown(f"### <span style='color:{color}'>{SKILL_LABELS.get(mode, mode)}</span>",
                        unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            c1.metric("Score", score)
            c2.metric("Steps", len(steps))
            c3.metric("Time", elapsed)

            # Verifier feedback
            vr = result.get("verifier_result", {})
            if vr:
                passed = vr.get("passed", False)
                feedback = vr.get("feedback", "")
                if passed:
                    st.success(f"PASSED: {feedback[:100]}")
                else:
                    st.error(f"FAILED: {feedback[:100]}")

                # Criteria breakdown table
                criteria_list = vr.get("criteria", [])
                if criteria_list:
                    st.caption("**Scoring Breakdown**")
                    for c in criteria_list:
                        name = c.get("name", "")
                        pts = c.get("points", 0)
                        earned = c.get("earned", 0)
                        if earned >= pts:
                            st.markdown(f"- :green[**{earned}/{pts}**] {name}")
                        elif earned > 0:
                            st.markdown(f"- :orange[**{earned}/{pts}**] {name}")
                        else:
                            st.markdown(f"- :red[**{earned}/{pts}**] {name}")

    st.divider()

    # -----------------------------------------------------------------------
    # Prompt / Skill section (collapsed)
    # -----------------------------------------------------------------------
    with st.expander("Task Prompt & Skill Content", expanded=False):
        pcols = st.columns(len(selected_modes))
        for pcol, mode in zip(pcols, selected_modes):
            with pcol:
                st.caption(SKILL_LABELS.get(mode, mode))
                prompt = load_prompt(exp, mode, software, task)
                st.text_area("Prompt", prompt[:5000], height=300,
                             key=f"prompt_{mode}", disabled=True)

    st.divider()

    # -----------------------------------------------------------------------
    # Trajectory: all steps, scrollable, side by side
    # -----------------------------------------------------------------------
    st.subheader("Trajectory")

    max_steps = max(len(mode_data[m]["steps"]) for m in selected_modes)

    for step_idx in range(max_steps):
        cols = st.columns(len(selected_modes))
        for col, mode in zip(cols, selected_modes):
            with col:
                steps = mode_data[mode]["steps"]
                if step_idx < len(steps):
                    render_step(
                        steps[step_idx], step_idx + 1,
                        exp, mode, software, task,
                        show_screenshot=show_screenshots,
                    )
                else:
                    st.caption("—")
        # Divider between steps
        if step_idx < max_steps - 1:
            st.markdown("---")


if __name__ == "__main__":
    main()
