# Daily Reflection Tree

A deterministic, rule‑based end‑of‑day reflection tool for employees.  
It guides users through a structured conversation based on three psychological axes:  
**Locus of Control**, **Contribution vs Entitlement**, and **Radius of Concern**.

No AI is used at runtime – all questions, branches, and reflections are pre‑defined in a JSON decision tree.  
This eliminates hallucinations and guarantees predictable, repeatable outcomes.

---

## 📁 Repository Structure

.
├── reflection-tree.json # The full decision tree (50+ nodes)
├── agent.py # CLI agent that walks the tree
├── generate_mermaid.py # (Optional) script to produce Mermaid diagram from JSON
├── persona-1-transcript.md # Example walkthrough (Victor / Contributor / Altrocentric)
├── README.md # This file
└── DESIGN.md # Design rationale and psychological framework

---

## 🚀 How to Run (Part B – Optional Agent)

1. **Ensure Python 3.7+** is installed.
2. Clone the repository and navigate to its folder.
3. Run the agent:
   ```bash
   python agent.py
   Answer the multiple‑choice questions as they appear.
   The agent remembers your choices, tracks “signals” (e.g., axis1:internal), and produces a personalised summary at the end.
   ```

Note: The agent is purely deterministic – it only loads reflection-tree.json and follows pre‑defined transitions. No external API calls, no LLM.
