"""Taxonomy tree data structure with max-depth constraint.

A taxonomy is a tree where:
- Root is at depth 0 (the domain, e.g., "chrome")
- Categories at depth 1
- Leaf topics at depth 2 (max_depth=3 means depths 0,1,2)

Each leaf has:
- signals: discovery sources that mapped here
- skill_status: "none" | "generated" | "refined"
- tasks: OS World task IDs classified to this node
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class TaxonomyNode:
    id: str
    name: str
    depth: int
    description: str = ""
    children: list[TaxonomyNode] = field(default_factory=list)
    # Leaf-only fields
    search_queries: list[str] = field(default_factory=list)  # YouTube search variants
    signals: list[str] = field(default_factory=list)
    skill_status: str = "none"  # "none" | "generated" | "refined"
    tasks: list[str] = field(default_factory=list)

    @property
    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def find(self, node_id: str) -> TaxonomyNode | None:
        """Find a node by ID (DFS)."""
        if self.id == node_id:
            return self
        for child in self.children:
            found = child.find(node_id)
            if found:
                return found
        return None

    def leaves(self) -> list[TaxonomyNode]:
        """Return all leaf nodes."""
        if self.is_leaf:
            return [self]
        result = []
        for child in self.children:
            result.extend(child.leaves())
        return result

    def to_dict(self) -> dict:
        d = {
            "id": self.id,
            "name": self.name,
            "depth": self.depth,
        }
        if self.description:
            d["description"] = self.description
        if self.children:
            d["children"] = [c.to_dict() for c in self.children]
        if self.search_queries:
            d["search_queries"] = self.search_queries
        if self.signals:
            d["signals"] = self.signals
        if self.skill_status != "none":
            d["skill_status"] = self.skill_status
        if self.tasks:
            d["tasks"] = self.tasks
        # Always include skill_status and tasks on leaves
        if self.is_leaf:
            d.setdefault("skill_status", "none")
            d.setdefault("tasks", [])
        return d

    @classmethod
    def from_dict(cls, d: dict) -> TaxonomyNode:
        children = [cls.from_dict(c) for c in d.get("children", [])]
        return cls(
            id=d["id"],
            name=d["name"],
            depth=d.get("depth", 0),
            description=d.get("description", ""),
            children=children,
            search_queries=d.get("search_queries", []),
            signals=d.get("signals", []),
            skill_status=d.get("skill_status", "none"),
            tasks=d.get("tasks", []),
        )

    def pretty(self, indent: str = "", last: bool = True) -> str:
        """Pretty-print the tree."""
        connector = "└── " if last else "├── "
        prefix = indent + connector if indent else ""
        label = self.name
        if self.is_leaf:
            label += f"  [{self.skill_status}]"
            if self.tasks:
                label += f"  ({len(self.tasks)} tasks)"
        line = prefix + label
        lines = [line]
        child_indent = indent + ("    " if last else "│   ")
        for i, child in enumerate(self.children):
            lines.append(child.pretty(child_indent, i == len(self.children) - 1))
        return "\n".join(lines)


@dataclass
class Taxonomy:
    domain: str
    version: int
    max_depth: int
    root: TaxonomyNode

    def save(self, path: Path) -> None:
        data = {
            "domain": self.domain,
            "version": self.version,
            "max_depth": self.max_depth,
            "root": self.root.to_dict(),
        }
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2) + "\n")

    @classmethod
    def load(cls, path: Path) -> Taxonomy:
        data = json.loads(path.read_text())
        return cls(
            domain=data["domain"],
            version=data["version"],
            max_depth=data["max_depth"],
            root=TaxonomyNode.from_dict(data["root"]),
        )

    def find(self, node_id: str) -> TaxonomyNode | None:
        return self.root.find(node_id)

    def leaves(self) -> list[TaxonomyNode]:
        return self.root.leaves()

    def print_tree(self) -> None:
        print(self.root.pretty())
