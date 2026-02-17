# WLM‑Knowledge‑Engine  
**Turn token soup → dimensional structure → reasoning‑ready knowledge graphs**

The **WLM‑Knowledge‑Engine** is the **knowledge structuring layer** of the WLM ecosystem.  
It transforms unstructured text into **dimensional knowledge structures** and then into  
**reasoning‑ready knowledge graphs** that AI systems can actually *understand* and *use*.

This is the **fifth major layer** of WLM:

1. SLP‑World‑Interpreter — Language → Structure  
2. WLM‑World‑Model‑Interpreter — World Model → Structure  
3. WLM‑Agent‑Behavior — Structure → Behavior  
4. WLM‑Persona‑Engine — Structure → Identity  
5. **WLM‑Knowledge‑Engine — Structure → Knowledge** ← *this repo*

It provides the missing link between **text** and **true understanding**:

> **Structure → Knowledge → Reasoning → World**

---

## ✨ Why this exists

LLMs do not “understand” knowledge.  
They interpolate token patterns.  
They memorize embeddings.  
They regurgitate correlations.

This leads to:

- hallucinations  
- contradictions  
- shallow reasoning  
- no global consistency  
- no causal structure  
- no dimensional grounding  

The WLM‑Knowledge‑Engine fixes this by converting text into:

- **dimensional structures**  
- **entity graphs**  
- **causal relations**  
- **temporal sequences**  
- **physical constraints**  
- **world‑consistent knowledge graphs**  

This is **knowledge as structure**, not as embeddings.

---

## ✨ Features

### **1. Dimensional Knowledge Extraction**
Extracts knowledge along WLM’s four core dimensions:

- **Spatial** — locations, topology, containment  
- **Temporal** — sequences, durations, dependencies  
- **Physical** — forces, constraints, affordances  
- **Causal** — preconditions, effects, mechanisms  

### **2. Knowledge Graph Construction**
Builds a **deterministic, interpretable knowledge graph**:

- nodes = entities  
- edges = dimensional relations  
- closures = predicted future states  
- tensions = contradictions or missing links  

### **3. Contradiction Detection**
Detects:

- logical conflicts  
- causal impossibilities  
- temporal inconsistencies  
- spatial contradictions  

### **4. Reasoning‑Ready Output**
Produces a graph that can be used by:

- agents  
- planners  
- simulators  
- reasoning engines  
- multi‑agent systems  

### **5. Deterministic Pipeline**
Same text → same structure → same knowledge graph.

---

## 🚀 Quickstart

### **Install**

```bash
pip install wlm-knowledge-engine
```

### **Use**

```python
from wlm_knowledge_engine import extract_knowledge

kg = extract_knowledge("The Earth orbits the Sun once every 365 days.")
print(kg)
```

### **Output (MVP)**

```
KnowledgeGraph {
  entities: ["Earth", "Sun"]
  relations: [
    orbit(Earth, Sun),
    period(Earth, 365 days)
  ]
  dimensions: { ... }
  tensions: []
  closures: []
}
```

---

## 🧠 How it works

The engine performs three steps:

### **1. Text → Dimensional Structure**
Extracts:

- entities  
- relations  
- events  
- causal links  
- temporal sequences  
- physical constraints  

### **2. Structure → Knowledge Graph**
Normalizes and merges:

- nodes  
- edges  
- dimensional annotations  
- closures  
- tensions  

### **3. Knowledge Graph → Reasoning Substrate**
Produces a graph that can be used for:

- causal reasoning  
- temporal reasoning  
- spatial reasoning  
- multi‑agent coordination  
- world model updates  

---

## 📦 API

### `extract_knowledge(text: str) → dict`

```python
def extract_knowledge(text: str) -> dict:
    """
    Convert raw text into a dimensional knowledge graph.
    """
```

### KnowledgeGraph structure (MVP)

```json
{
  "entities": [],
  "relations": [],
  "dimensions": {},
  "tensions": [],
  "closures": []
}
```

---

## 📘 Examples

### Example: Simple Fact

**Input**

```
Water boils at 100°C.
```

**Output**

```
entity: Water
relation: boils_at(Water, 100°C)
dimension: physical
```

---

## 🏗 Repository Structure

```
wlm-knowledge-engine/
│
├── LICENSE
├── README.md
├── pyproject.toml
├── setup.cfg
│
├── src/
│   └── wlm_knowledge_engine/
│       ├── __init__.py
│       ├── api.py
│       ├── extractor.py
│       ├── dimension_engine.py
│       ├── graph_builder.py
│       ├── tension_detector.py
│       ├── closure_predictor.py
│       └── cli.py
│
├── examples/
│   ├── simple_fact.md
│   ├── causal_chain.md
│   └── temporal_sequence.md
│
├── tests/
│   ├── test_extractor.py
│   ├── test_graph_builder.py
│   ├── test_dimension_engine.py
│   └── test_end_to_end.py
│
└── docs/
    ├── overview.md
    ├── knowledge-rules.md
    ├── api.md
    └── roadmap.md
```

---

## 📄 License

MIT License  
Copyright (c) 2026  
**Wujie Gu**

---

## 🧩 Summary

The **WLM‑Knowledge‑Engine** is the structural knowledge layer of the WLM ecosystem.  
It turns text into **dimensional structure**, then into **reasoning‑ready knowledge graphs**.

It enables:

- real understanding  
- causal reasoning  
- temporal reasoning  
- spatial reasoning  
- consistent world models  
- agents that actually know things  

A foundational component of the **WLM knowledge stack**.
