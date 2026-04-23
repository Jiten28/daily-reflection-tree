#!/usr/bin/env python3
"""
Daily Reflection Tree — CLI Agent
Walks reflection-tree.json deterministically.
No LLM calls at runtime. Pure tree traversal + state accumulation.
"""

import json
import sys
import os
import time
from typing import Optional

TREE_PATH = os.path.join(os.path.dirname(
    __file__), "../tree/reflection-tree.json")
SLOW_PRINT = True  # Set False for instant output (useful during testing)


# ── Helpers ─────────────────────────────────────────────────────────────────

def slow_print(text: str, delay: float = 0.025) -> None:
    if not SLOW_PRINT:
        print(text)
        return
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def divider(char: str = "─", width: int = 60) -> None:
    print(char * width)


def clear_line() -> None:
    print()


def interpolate(text: str, state: dict) -> str:
    """Replace {NODE_ID.answer} and {axis.dominant} placeholders."""
    for node_id, answer in state.get("answers", {}).items():
        text = text.replace(f"{{{node_id}.answer}}", answer)
    for axis in ["axis1", "axis2", "axis3"]:
        dominant = state.get("signals", {}).get(axis, {})
        if dominant:
            dominant_pole = max(dominant, key=dominant.get)
            templates = state["summary_templates"].get(axis, {})
            label = templates.get(dominant_pole, dominant_pole)
            text = text.replace(f"{{{axis}.dominant}}", label)
    # Tomorrow question
    key = _build_tomorrow_key(state)
    tmpl = state["summary_templates"].get("tomorrow_questions", {})
    question = tmpl.get(key, tmpl.get(
        "mixed_mixed_mixed", "What one thing would make tomorrow better than today?"))
    text = text.replace("{tomorrow_question}", question)
    return text


def _build_tomorrow_key(state: dict) -> str:
    parts = []
    for axis in ["axis1", "axis2", "axis3"]:
        dominant = state.get("signals", {}).get(axis, {})
        if dominant:
            parts.append(max(dominant, key=dominant.get))
        else:
            parts.append("mixed")
    return "_".join(parts)


# ── Node resolution ──────────────────────────────────────────────────────────

def get_node(nodes: dict, node_id: str) -> Optional[dict]:
    return nodes.get(node_id)


def record_signal(state: dict, signal: Optional[str]) -> None:
    if not signal:
        return
    axis, pole = signal.split(":")
    state["signals"].setdefault(axis, {})
    state["signals"][axis][pole] = state["signals"][axis].get(pole, 0) + 1


def resolve_decision(node: dict, state: dict) -> Optional[str]:
    """Evaluate routing rules and return next node id."""
    for rule in node["options"]:
        if rule.startswith("answer="):
            # Format: answer=Val1|Val2:TARGET
            rest = rule[len("answer="):]
            values_part, target = rest.rsplit(":", 1)
            values = values_part.split("|")
            last_question_answer = state.get("last_answer", "")
            if last_question_answer in values:
                return target
        elif rule.startswith("signal_dominant="):
            # Format: signal_dominant=axis:pole:TARGET
            rest = rule[len("signal_dominant="):]
            parts = rest.split(":")
            axis, pole, target = parts[0], parts[1], parts[2]
            dominant = state.get("signals", {}).get(axis, {})
            if dominant:
                dom_pole = max(dominant, key=dominant.get)
                if dom_pole == pole:
                    return target
    return None


def find_children(nodes: dict, parent_id: str) -> list:
    return [n for n in nodes.values() if n.get("parentId") == parent_id]


def get_next_node_id(node: dict, nodes: dict, state: dict) -> Optional[str]:
    """Given current node, figure out the next node id."""
    nid = node["id"]
    node_type = node["type"]

    # Explicit target takes priority
    if node.get("target"):
        return node["target"]

    # Decision nodes route via rules
    if node_type == "decision":
        return resolve_decision(node, state)

    # Find single child
    children = find_children(nodes, nid)
    if len(children) == 1:
        return children[0]["id"]
    if len(children) > 1:
        # Multiple children — shouldn't happen for non-decision; pick first
        return children[0]["id"]
    return None


# ── Node rendering ───────────────────────────────────────────────────────────

def render_start(node: dict, state: dict) -> None:
    clear_line()
    divider("═")
    slow_print(f"  🌿  {interpolate(node['text'], state)}")
    divider("═")
    clear_line()
    input("  Press Enter to begin...")
    clear_line()


def render_question(node: dict, state: dict) -> str:
    clear_line()
    divider()
    slow_print(f"  {interpolate(node['text'], state)}")
    clear_line()
    options = node["options"]
    for i, opt in enumerate(options, 1):
        print(f"  [{i}] {opt}")
    clear_line()
    while True:
        try:
            raw = input("  Your answer (number): ").strip()
            idx = int(raw) - 1
            if 0 <= idx < len(options):
                chosen = options[idx]
                state["answers"][node["id"]] = chosen
                state["last_answer"] = chosen
                return chosen
            else:
                print(f"  Please enter a number between 1 and {len(options)}.")
        except (ValueError, KeyboardInterrupt):
            print("  Please enter a valid number.")


def render_reflection(node: dict, state: dict) -> None:
    clear_line()
    divider("·")
    slow_print(f"  💭  {interpolate(node['text'], state)}", delay=0.018)
    divider("·")
    clear_line()
    input("  (Press Enter to continue...)")
    clear_line()


def render_bridge(node: dict, state: dict) -> None:
    clear_line()
    slow_print(f"  ↳  {interpolate(node['text'], state)}", delay=0.02)
    clear_line()
    time.sleep(0.6)


def render_summary(node: dict, state: dict) -> None:
    clear_line()
    divider("═")
    slow_print("  📋  SESSION SUMMARY", delay=0.03)
    divider("═")
    slow_print(interpolate(node["text"], state), delay=0.015)
    divider("═")
    clear_line()
    input("  (Press Enter to close...)")
    clear_line()


def render_end(node: dict, state: dict) -> None:
    clear_line()
    slow_print(f"  🌙  {interpolate(node['text'], state)}")
    clear_line()


# ── Main walk ────────────────────────────────────────────────────────────────

def walk_tree(tree_data: dict) -> None:
    raw_nodes = tree_data["nodes"]
    nodes = {n["id"]: n for n in raw_nodes}

    state = {
        "answers": {},
        "last_answer": "",
        "signals": {},
        "summary_templates": tree_data.get("summary_templates", {})
    }

    current_id = "START"

    while current_id:
        node = get_node(nodes, current_id)
        if not node:
            print(f"[ERROR] Node '{current_id}' not found in tree. Stopping.")
            break

        ntype = node["type"]

        # Record signal if present
        record_signal(state, node.get("signal"))

        # Render based on type
        if ntype == "start":
            render_start(node, state)
        elif ntype == "question":
            render_question(node, state)
        elif ntype == "decision":
            pass  # invisible, no render
        elif ntype == "reflection":
            render_reflection(node, state)
        elif ntype == "bridge":
            render_bridge(node, state)
        elif ntype == "summary":
            render_summary(node, state)
        elif ntype == "end":
            render_end(node, state)
            break
        else:
            print(f"[WARN] Unknown node type '{ntype}' — skipping.")

        # Advance
        current_id = get_next_node_id(node, nodes, state)


def main():
    global SLOW_PRINT
    if "--fast" in sys.argv:
        SLOW_PRINT = False

    tree_path = TREE_PATH
    if not os.path.exists(tree_path):
        print(f"Error: tree file not found at {tree_path}")
        sys.exit(1)

    with open(tree_path, "r", encoding="utf-8") as f:
        tree_data = json.load(f)

    print("\n" * 2)
    walk_tree(tree_data)
    print("\n")


if __name__ == "__main__":
    main()
