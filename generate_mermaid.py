"""Generate a Mermaid diagram from a reflection tree JSON file."""
import json

with open("reflection_tree.json", "r", encoding="utf-8") as f:
    data = json.load(f)

nodes = {n["id"]: n for n in data["nodes"]}
print("```mermaid\ngraph TD")

for nid, node in nodes.items():
    if node["type"] in ["start", "question", "reflection", "bridge", "summary", "end"]:
        shape = "([" + nid + "])" if node["type"] in ["start",
                                                      "end", "summary"] else "(" + nid + ")"
        print(f"    {nid}{shape}")
    else:
        # decision nodes as diamonds
        print(f"    {nid}{{decision}}")

for nid, node in nodes.items():
    if node.get("target"):
        print(f"    {nid} --> {node['target']}")
    elif node.get("next") and isinstance(node["next"], dict):
        for opt, target in node["next"].items():
            print(f"    {nid} -->|{opt[:20]}...| {target}")
    elif node.get("options") and node["type"] == "decision":
        for opt in node["options"]:
            if ":" in opt:
                target = opt.split(":")[-1]
                print(f"    {nid} --> {target}")

print("```")
