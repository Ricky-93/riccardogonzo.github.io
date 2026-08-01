#!/usr/bin/env python3
"""Build a self-contained collaboration network from _publications/*.md.

Dependencies:
    pip install pyyaml

Run from the repository root:
    python tools/build_collaboration_network.py
"""

from __future__ import annotations

import html
import json
from pathlib import Path
from urllib.parse import quote

import yaml

ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS = ROOT / "_publications"
OUTPUT = ROOT / "collab_net" / "network.html"


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"{path}: missing YAML front matter")
    _, raw, _ = text.split("---", 2)
    return yaml.safe_load(raw) or {}


def main() -> None:
    nodes: list[dict] = []
    edges: list[dict] = []
    node_ids: dict[tuple[str, str], int] = {}
    next_id = 1

    def add_node(kind: str, label: str, **extra) -> int:
        nonlocal next_id
        key = (kind, label)
        if key in node_ids:
            return node_ids[key]
        node_id = next_id
        next_id += 1
        node_ids[key] = node_id
        nodes.append({"id": node_id, "label": label, "kind": kind, **extra})
        return node_id

    for path in sorted(PUBLICATIONS.glob("*.md")):
        data = front_matter(path)
        title = str(data.get("title", path.stem))
        published = bool(data.get("paperurl"))
        paper_id = add_node(
            "journal" if published else "preprint",
            title,
            url=str(data.get("paperurl") or data.get("preprinturl") or f"/publication/{path.stem}/"),
            title_text=str(data.get("venue") or "Preprint"),
        )
        authors = [a.strip() for a in str(data.get("authors", "")).split(",") if a.strip()]
        for author in authors:
            url = (
                "https://inspirehep.net/literature?"
                + "sort=mostrecent&q="
                + quote(f'a "{author}"')
            )
            author_id = add_node(
                "self" if author == "Riccardo Gonzo" else "author",
                author,
                url=url,
                title_text="Author",
            )
            edges.append({"from": author_id, "to": paper_id})

    payload_nodes = json.dumps(nodes, ensure_ascii=False)
    payload_edges = json.dumps(edges, ensure_ascii=False)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
<style>html,body,#network{height:100%;margin:0}</style>
</head>
<body>
<div id="network"></div>
<script>
const nodes = new vis.DataSet(__NODES__);
const edges = new vis.DataSet(__EDGES__);
const options = {
  nodes: {shape: "dot", font: {size: 13}},
  edges: {color: {color: "#c5c5c5"}, width: 1},
  groups: {
    self: {color: {background: "#a96f16", border: "#7f500e"}, size: 20},
    author: {color: {background: "#d6d2d2", border: "#888888"}, size: 10},
    preprint: {color: {background: "#79addc", border: "#2c6077"}, shape: "box"},
    journal: {color: {background: "#9e1910", border: "#64100b"}, font: {color: "white"}, shape: "box"}
  },
  physics: {stabilization: true, barnesHut: {gravitationalConstant: -4000}},
  interaction: {hover: true, navigationButtons: true}
};
const network = new vis.Network(document.getElementById("network"), {nodes, edges}, options);
network.on("doubleClick", params => {
  if (!params.nodes.length) return;
  const node = nodes.get(params.nodes[0]);
  if (node.url) window.open(node.url, "_blank", "noopener");
});
</script>
</body>
</html>
""".replace("__NODES__", payload_nodes).replace("__EDGES__", payload_edges),
        encoding="utf-8",
    )
    print(f"Wrote {OUTPUT} with {len(nodes)} nodes and {len(edges)} edges.")


if __name__ == "__main__":
    main()
