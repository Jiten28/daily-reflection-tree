# Daily Reflection Tree

A deterministic, rule‑based end‑day reflection tool for employees, built as a decision tree.  
It guides users through the three psychological axes: **Locus of Control**, **Contribution vs Entitlement**, and **Radius of Concern**.

> ✅ Part A (mandatory) and Part B (optional agent) are both fully implemented.  
> No AI is used at runtime – guaranteed deterministic, no hallucinations.

---

## 📁 Repository Contents

| File | Description |
|------|-------------|
| `reflection_tree.json` | The full decision tree (46 nodes, all required types) |
| `agent.py` | CLI agent that walks the tree deterministically |
| `README.md` | This file – overview, usage, diagram, and submission notes |
| `DESIGN.md` | Design rationale, psychological framework, guardrails |
| `persona-1-transcript.md` | Example session (Victor / Contributor / Altrocentric) |
| `generate_mermaid.py` | (Optional) script to regenerate the Mermaid diagram from JSON |
| `tree-diagram.mmd` | Standalone Mermaid diagram file |

---

## 🚀 How to Run the Agent (Part B)

1. **Ensure Python 3.7+** is installed.
2. Clone this repository and navigate into the folder.
3. Run the agent:
   ```bash
   python agent.py
4. Answer the multiple‑choice questions – the tool will remember your answers, compute signals, and produce a personalised summary at the end.

> The agent uses only standard library – no external packages.
> All branches are predetermined; the same inputs always lead to the same path.

---

## 🌳 Decision Tree Diagram (Mermaid)
Below is the full visual representation of the tree.
It starts with an opening question, branches through Locus → Orientation → Radius, and ends with a summary.

```mermaid
graph TD
    START([START])
    OPEN_Q1(OPEN_Q1)
    OPEN_D1{decision}
    A1_Q_AGENCY_HIGH(A1_Q_AGENCY_HIGH)
    A1_Q_AGENCY_MID(A1_Q_AGENCY_MID)
    A1_Q_AGENCY_LOW(A1_Q_AGENCY_LOW)
    A1_D2{decision}
    A1_D3{decision}
    A1_D4{decision}
    A1_Q_CHOICE_INTERNAL(A1_Q_CHOICE_INTERNAL)
    A1_Q_CHOICE_MIXED(A1_Q_CHOICE_MIXED)
    A1_Q_CHOICE_EXTERNAL(A1_Q_CHOICE_EXTERNAL)
    A1_REFLECT_D{decision}
    A1_REFLECTION_INTERNAL(A1_REFLECTION_INTERNAL)
    A1_REFLECTION_EXTERNAL(A1_REFLECTION_EXTERNAL)
    A1_REFLECTION_MIXED(A1_REFLECTION_MIXED)
    BRIDGE_1_2(BRIDGE_1_2)
    A2_OPEN(A2_OPEN)
    A2_D1{decision}
    A2_Q_CONTRIBUTION(A2_Q_CONTRIBUTION)
    A2_Q_ENTITLEMENT(A2_Q_ENTITLEMENT)
    A2_D2{decision}
    A2_D3{decision}
    A2_Q_DISCRETIONARY(A2_Q_DISCRETIONARY)
    A2_Q_AWARENESS(A2_Q_AWARENESS)
    A2_REFLECT_D{decision}
    A2_REFLECTION_CONTRIBUTION(A2_REFLECTION_CONTRIBUTION)
    A2_REFLECTION_ENTITLEMENT(A2_REFLECTION_ENTITLEMENT)
    A2_REFLECTION_MIXED(A2_REFLECTION_MIXED)
    BRIDGE_2_3(BRIDGE_2_3)
    A3_OPEN(A3_OPEN)
    A3_D1{decision}
    A3_Q_SELF(A3_Q_SELF)
    A3_Q_TEAM(A3_Q_TEAM)
    A3_Q_OTHER(A3_Q_OTHER)
    A3_D2{decision}
    A3_D3{decision}
    A3_D4{decision}
    A3_Q_TRANSCEND(A3_Q_TRANSCEND)
    A3_Q_MEANING(A3_Q_MEANING)
    A3_REFLECT_D{decision}
    A3_REFLECTION_ALTRO(A3_REFLECTION_ALTRO)
    A3_REFLECTION_TEAM(A3_REFLECTION_TEAM)
    A3_REFLECTION_SELF(A3_REFLECTION_SELF)
    SUMMARY([SUMMARY])
    END([END])
    START --> OPEN_Q1
    OPEN_D1 --> A1_Q_AGENCY_HIGH
    OPEN_D1 --> A1_Q_AGENCY_MID
    OPEN_D1 --> A1_Q_AGENCY_LOW
    OPEN_D1 --> A1_Q_AGENCY_MID
    A1_D2 --> A1_Q_CHOICE_INTERNAL
    A1_D2 --> A1_Q_CHOICE_INTERNAL
    A1_D2 --> A1_Q_CHOICE_MIXED
    A1_D2 --> A1_Q_CHOICE_EXTERNAL
    A1_D3 --> A1_Q_CHOICE_INTERNAL
    A1_D3 --> A1_Q_CHOICE_MIXED
    A1_D3 --> A1_Q_CHOICE_MIXED
    A1_D3 --> A1_Q_CHOICE_EXTERNAL
    A1_D4 --> A1_Q_CHOICE_EXTERNAL
    A1_D4 --> A1_Q_CHOICE_MIXED
    A1_D4 --> A1_Q_CHOICE_MIXED
    A1_D4 --> A1_Q_CHOICE_EXTERNAL
    A1_REFLECT_D --> A1_REFLECTION_INTERNAL
    A1_REFLECT_D --> A1_REFLECTION_EXTERNAL
    A1_REFLECT_D --> A1_REFLECTION_MIXED
    A1_REFLECTION_INTERNAL --> BRIDGE_1_2
    A1_REFLECTION_EXTERNAL --> BRIDGE_1_2
    A1_REFLECTION_MIXED --> BRIDGE_1_2
    BRIDGE_1_2 --> A2_OPEN
    A2_D1 --> A2_Q_CONTRIBUTION
    A2_D1 --> A2_Q_ENTITLEMENT
    A2_D1 --> A2_Q_CONTRIBUTION
    A2_D1 --> A2_Q_ENTITLEMENT
    A2_D2 --> A2_Q_DISCRETIONARY
    A2_D2 --> A2_Q_DISCRETIONARY
    A2_D2 --> A2_Q_DISCRETIONARY
    A2_D2 --> A2_Q_AWARENESS
    A2_D3 --> A2_Q_AWARENESS
    A2_D3 --> A2_Q_AWARENESS
    A2_D3 --> A2_Q_AWARENESS
    A2_D3 --> A2_Q_DISCRETIONARY
    A2_REFLECT_D --> A2_REFLECTION_CONTRIBUTION
    A2_REFLECT_D --> A2_REFLECTION_ENTITLEMENT
    A2_REFLECT_D --> A2_REFLECTION_MIXED
    A2_REFLECTION_CONTRIBUTION --> BRIDGE_2_3
    A2_REFLECTION_ENTITLEMENT --> BRIDGE_2_3
    A2_REFLECTION_MIXED --> BRIDGE_2_3
    BRIDGE_2_3 --> A3_OPEN
    A3_D1 --> A3_Q_SELF
    A3_D1 --> A3_Q_TEAM
    A3_D1 --> A3_Q_OTHER
    A3_D1 --> A3_Q_OTHER
    A3_D2 --> A3_Q_TRANSCEND
    A3_D2 --> A3_Q_MEANING
    A3_D2 --> A3_Q_MEANING
    A3_D2 --> A3_Q_TRANSCEND
    A3_D3 --> A3_Q_TRANSCEND
    A3_D3 --> A3_Q_MEANING
    A3_D3 --> A3_Q_MEANING
    A3_D3 --> A3_Q_MEANING
    A3_D4 --> A3_Q_TRANSCEND
    A3_D4 --> A3_Q_TRANSCEND
    A3_D4 --> A3_Q_TRANSCEND
    A3_D4 --> A3_Q_MEANING
    A3_REFLECT_D --> A3_REFLECTION_ALTRO
    A3_REFLECT_D --> A3_REFLECTION_TEAM
    A3_REFLECT_D --> A3_REFLECTION_SELF
    A3_REFLECTION_ALTRO --> SUMMARY
    A3_REFLECTION_TEAM --> SUMMARY
    A3_REFLECTION_SELF --> SUMMARY
    SUMMARY --> END
```

(Diagram automatically generated from ```reflection-tree.json```)

## ✅ Part A (Mandatory) Deliverables

| Requirement | Status |
| :--- | :--- |
| **Structured data** (JSON) with ≥25 nodes | ✅ 46 nodes |
| **Node types**: start, question (≥8), decision (≥4), reflection (≥4), bridge (≥2), summary, end | ✅ All present |
| **Three psychological axes** in order: Locus → Orientation → Radius | ✅ Axes 1,2,3 |
| **Visual diagram** (Mermaid or draw.io) | ✅ Above + tree-diagram.mmd |
| **Design write‑up** (≤2 pages) | ✅ DESIGN.md |

## 🤖 Part B (Optional) – Completed
The CLI agent ```(agent.py)``` is fully functional:

Loads the decision tree from JSON.

Walks through every node deterministically.

Tracks signals (```axis1:internal```, etc.) and calculates dominant poles.

Outputs a personalised summary with a “question for tomorrow” based on the user’s path.

Example transcript is provided in ```persona-1-transcript.md```.
You can generate another by running the agent with different answers.

## 📦 Dependencies
Python 3.7+ (standard library only – no external packages)

## 🛡️ Guardrails Against AI Hallucination
**No runtime AI** – all questions, options, reflections, and routing logic are pre‑written in JSON.

**Deterministic branching** – based on exact string matching or signal dominance counts (integers).

**Static summary templates** – only placeholders are substituted; no generative text.

This meets the assignment’s requirement to eliminate hallucination risk.

## 📖 Further Reading
```DESIGN.md``` – detailed psychological framework, node count verification, and design trade‑offs.

```persona-1-transcript.md``` – a complete walkthrough showing a Victor / Contributor / Altrocentric path.

## 📄 License & Author

This project is submitted as a recruitment assignment for **DeepThought / DTCultureTech**.  
All rights reserved to the author.

**Jiten Kumar**  
📧 work.jiten282003@gmail.com  
🌐 [Portfolio](https://jitenkumarportfolio.netlify.app)  
🔗 [LinkedIn](https://linkedin.com/in/jiten-kumar-85a03217a)
