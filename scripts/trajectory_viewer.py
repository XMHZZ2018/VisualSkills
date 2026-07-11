"""
Trajectory Viewer — Streamlit app for comparing agent runs across skill modes.

Runs on the VM (in tmux session `viewer`) and reads workspaces directly.
Access locally via SSH tunnel: `ssh -fN -L 8502:127.0.0.1:8502 osexpert`.

Usage on VM:
    streamlit run scripts/trajectory_viewer.py --server.port 8502 --server.address 127.0.0.1 --server.headless true
"""
import json
from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
WORKSPACE_ROOTS = {
    "cua-world": "/home/ziyan/MMSkills/scripts/run-cua-world/workspaces",
    "osexpert (OSExpert)": "/home/ziyan/MMSkills/scripts/run-osexpert/workspaces",
}
WORKSPACE_ROOT = WORKSPACE_ROOTS["cua-world"]

SKILL_MODES = [
    "skill-none",
    "skill-text",
    "skill-text-v2",
    "skill-multimodal",
    "skill-multimodal-v0",
    "skill-multimodal-v2",
    "skill-multimodal-loader",
]
SKILL_LABELS = {
    "skill-none": "No Skill",
    "skill-text": "Text Skill (v1)",
    "skill-text-v2": "Text Skill (v2)",
    "skill-multimodal": "Multimodal Skill (v1)",
    "skill-multimodal-v0": "Multimodal Skill (v0: v1 + UI ref)",
    "skill-multimodal-v2": "Multimodal Skill (v2)",
    "skill-multimodal-loader": "Multimodal Skill (loader, load_topic MCP)",
}
MODE_COLORS = {
    "skill-none": "#ff6b6b",
    "skill-text": "#4ecdc4",
    "skill-text-v2": "#2b9348",
    "skill-multimodal": "#45b7d1",
    "skill-multimodal-v0": "#8338ec",
    "skill-multimodal-v2": "#2a9d8f",
    "skill-multimodal-loader": "#f4a261",
}


# ---------------------------------------------------------------------------
# Filesystem helpers (viewer runs on the VM; reads workspaces directly)
# ---------------------------------------------------------------------------
@st.cache_data(ttl=120)
def list_dir(path: str) -> list[str]:
    try:
        return sorted(p.name for p in Path(path).iterdir())
    except (FileNotFoundError, NotADirectoryError):
        return []


@st.cache_data(ttl=300)
def read_file(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return ""


@st.cache_data(ttl=600)
def read_image(path: str) -> bytes:
    try:
        return Path(path).read_bytes()
    except FileNotFoundError:
        return b""


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------
def list_experiments() -> list[str]:
    return list_dir(WORKSPACE_ROOT)


def list_available_modes(exp: str) -> list[str]:
    dirs = list_dir(f"{WORKSPACE_ROOT}/{exp}")
    return [d for d in SKILL_MODES if d in dirs]


def list_softwares(exp: str, mode: str) -> list[str]:
    return list_dir(f"{WORKSPACE_ROOT}/{exp}/{mode}")


def list_tasks(exp: str, mode: str, software: str) -> list[str]:
    return list_dir(f"{WORKSPACE_ROOT}/{exp}/{mode}/{software}")


def list_screenshots(exp: str, mode: str, software: str, task: str) -> list[str]:
    path = f"{WORKSPACE_ROOT}/{exp}/{mode}/{software}/{task}/screenshots"
    return [f for f in list_dir(path) if f.endswith(".png")]


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
@st.cache_data(ttl=300)
def load_result(exp: str, mode: str, software: str, task: str) -> dict:
    base = f"{WORKSPACE_ROOT}/{exp}/{mode}/{software}/{task}"
    # Preferred (CUA-World): result.json
    text = read_file(f"{base}/result.json")
    if text:
        try:
            return json.loads(text)
        except (json.JSONDecodeError, ValueError):
            pass
    # OSExpert layout: meta.json + result.txt (alias `result` → `score`)
    meta_text = read_file(f"{base}/meta.json")
    if meta_text:
        try:
            d = json.loads(meta_text)
            if "result" in d and "score" not in d:
                d["score"] = d["result"]
            return d
        except (json.JSONDecodeError, ValueError):
            pass
    score_text = read_file(f"{base}/result.txt").strip()
    if score_text:
        try:
            return {"score": float(score_text)}
        except ValueError:
            return {"score": score_text}
    return {}


@st.cache_data(ttl=600)
def load_task_json(software: str, task: str) -> dict:
    """Load task.json from the CUA-World tasks directory on the VM."""
    ga_tasks = (
        "/home/ziyan/MMSkills/vendor/gym-anything/benchmarks/cua_world"
        f"/environments/{software}/tasks/{task}/task.json"
    )
    text = read_file(ga_tasks)
    try:
        return json.loads(text)
    except (json.JSONDecodeError, ValueError):
        return {}


@st.cache_data(ttl=300)
def load_prompt(exp: str, mode: str, software: str, task: str) -> str:
    path = f"{WORKSPACE_ROOT}/{exp}/{mode}/{software}/{task}/prompt.txt"
    return read_file(path)


MCP_PREFIXES = ("mcp__cua-world-controller__", "mcp__osexpert-controller__")
# Tools that are internal to Claude CLI, not GUI actions and not worth showing
SKIP_TOOLS = {"ToolSearch"}
# Tools that read files; we fold these into the following GUI step as
# "preparation reads" rather than rendering them as their own steps.
FILE_READ_TOOLS = {"Read", "Glob", "Grep"}
# Substrings that identify a skill-directory read (vs. a task-input read).
SKILL_PATH_MARKERS = ("/plugin/", "/skills/", "/.claude/plugins/")


def _is_skill_path(fp: str) -> bool:
    return any(m in fp for m in SKILL_PATH_MARKERS)


def _format_read(tool_name: str, tool_input: dict) -> tuple[str, str, bool]:
    """Return (short_name, file_basename, is_skill) for a file-read tool call."""
    short = tool_name
    if short == "Read":
        fp = tool_input.get("file_path", "")
    elif short == "Glob":
        fp = tool_input.get("pattern", "")
    elif short == "Grep":
        fp = tool_input.get("path", "") or tool_input.get("pattern", "")
    else:
        fp = ""
    basename = fp.split("/")[-1] if "/" in fp else fp
    return short, basename, _is_skill_path(fp)


def _format_action(tool_name: str, tool_input: dict) -> tuple[str, str]:
    """Return (short_name, detail) for a GUI action tool call."""
    short = tool_name
    for _p in MCP_PREFIXES:
        if short.startswith(_p):
            short = short[len(_p):]
            break
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
    return short, detail


@st.cache_data(ttl=300)
def parse_trajectory(exp: str, mode: str, software: str, task: str) -> list[dict]:
    """Parse claude_output.txt into a list of agent steps.

    A "step" is one MCP (GUI) tool call. Non-MCP reads (Read/Glob/Grep) that
    precede a step are folded into it as `reads_before` so they don't inflate
    the step count. Reads that hit the skill/plugin directory are labeled
    `is_skill=True`; others (e.g. task inputs like json_snippet.txt) are plain
    file reads.

    Screenshot files on disk (`step_NNN.png`) are named by the bridge's
    per-`/screenshot`-call counter (bridge.py:136). The MCP server's
    `_action_and_screenshot` (tools/cua-world-controller/server.py:76)
    calls `/screenshot` after every action, and the explicit `screenshot`
    tool does the same. So effectively every MCP tool call produces one
    `step_{k:03d}.png` where k is the MCP-call index.
    """
    path = f"{WORKSPACE_ROOT}/{exp}/{mode}/{software}/{task}/claude_output.txt"
    raw = read_file(path)
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

    # Pass 0: map tool_use_id → whether its result carried an image. Only tool
    # calls whose result contains an image actually produced a step_NNN.png on
    # disk; the rest (failed /screenshot calls, errored actions) did not.
    tool_use_has_image: dict[str, bool] = {}
    for ev in events:
        if ev.get("type") != "user":
            continue
        content = ev.get("message", {}).get("content", [])
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict) or block.get("type") != "tool_result":
                continue
            tid = block.get("tool_use_id", "")
            rc = block.get("content", [])
            has_img = False
            if isinstance(rc, list):
                has_img = any(
                    isinstance(c, dict) and c.get("type") == "image"
                    for c in rc
                )
            tool_use_has_image[tid] = has_img

    steps = []
    pending_reads = []      # file-reads waiting to attach to next GUI step
    cur_thinking = []
    cur_text = []
    screenshot_idx = 0      # increments only when an image was actually saved

    for ev in events:
        if ev.get("type") != "assistant":
            continue
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
                name = block.get("name", "")
                inp = block.get("input", {})

                if name in SKIP_TOOLS:
                    continue

                if name in FILE_READ_TOOLS:
                    short, basename, is_skill = _format_read(name, inp)
                    pending_reads.append({
                        "tool": short,
                        "target": basename,
                        "is_skill": is_skill,
                    })
                    continue

                if not any(name.startswith(p) for p in MCP_PREFIXES):
                    # Unknown non-MCP tool — show as a read for visibility.
                    pending_reads.append({
                        "tool": name, "target": "", "is_skill": False,
                    })
                    continue

                # GUI action = one step. Every *successful* MCP call triggers
                # a `/screenshot` on the bridge and saves one file. If the
                # action errored or /screenshot failed, no image came back —
                # those calls don't advance the disk counter.
                short, detail = _format_action(name, inp)
                tid = block.get("id", "")
                if tool_use_has_image.get(tid, False):
                    screenshot_idx += 1
                    screenshot_file = f"step_{screenshot_idx:03d}.png"
                else:
                    screenshot_file = None

                steps.append({
                    "thinking": "\n\n".join(t for t in cur_thinking if t),
                    "text": "\n".join(t for t in cur_text if t),
                    "action": short,
                    "action_detail": detail,
                    "action_input": inp,
                    "screenshot_file": screenshot_file,
                    "reads_before": pending_reads,
                })
                pending_reads = []
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

    # Preparation reads that preceded this action (skill files, task inputs, ...)
    reads = step.get("reads_before", [])
    if reads:
        skill_reads = [r for r in reads if r["is_skill"]]
        other_reads = [r for r in reads if not r["is_skill"]]
        parts = []
        if skill_reads:
            items = ", ".join(f"`{r['target']}`" for r in skill_reads)
            parts.append(f":green[loaded skill:] {items}")
        if other_reads:
            items = ", ".join(
                f"`{r['target']}`" if r["target"] else f"`{r['tool']}`"
                for r in other_reads
            )
            parts.append(f":gray[read:] {items}")
        st.caption(" · ".join(parts))

    # Thinking
    if step["thinking"]:
        with st.expander("Thinking", expanded=False):
            st.markdown(step["thinking"][:3000])

    # Text response
    if step["text"]:
        st.caption(step["text"][:500])

    # Every MCP call produces its own screenshot (captured by the bridge
    # after the action); it shows the state *after* this step.
    if show_screenshot:
        fname = step.get("screenshot_file")
        if fname:
            path = f"{WORKSPACE_ROOT}/{exp}/{mode}/{software}/{task}/screenshots/{fname}"
            try:
                img_bytes = read_image(path)
                if img_bytes:
                    st.image(img_bytes, caption=fname, use_container_width=True)
            except Exception:
                pass


def main():
    st.set_page_config(page_title="MMSkills Trajectory Viewer", layout="wide")
    st.title("MMSkills Trajectory Viewer")

    # Sidebar: selection
    with st.sidebar:
        st.header("Select Run")

        benchmark = st.selectbox("Benchmark", list(WORKSPACE_ROOTS.keys()))
        global WORKSPACE_ROOT
        WORKSPACE_ROOT = WORKSPACE_ROOTS[benchmark]

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
    if not task_json:
        # OSExpert/etc.: pull instruction from any selected mode's meta.json
        for _m in selected_modes:
            _r = load_result(exp, _m, software, task)
            _instr = _r.get("instruction")
            if _instr:
                st.subheader("Task")
                st.markdown(f"**{task}**")
                st.info(_instr)
                st.divider()
                break
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
                            col = cols_meta[i % len(cols_meta)]
                            if isinstance(v, list):
                                col.markdown(
                                    f"**{label}:**\n" + "\n".join(f"- {item}" for item in v))
                            elif isinstance(v, dict):
                                lines = [f"- `{kk}`: {vv}" for kk, vv in v.items()]
                                col.markdown(f"**{label}:**\n" + "\n".join(lines))
                            elif isinstance(v, (str, int, float)):
                                col.metric(label, v)
                            else:
                                col.markdown(f"**{label}:** `{v}`")

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
