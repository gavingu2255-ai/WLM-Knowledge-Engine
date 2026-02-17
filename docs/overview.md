# WLM‑Knowledge‑Engine — Overview  
**Text → Dimensional Structure → Reasoning‑Ready Knowledge Graphs**

The **WLM‑Knowledge‑Engine** is the knowledge structuring layer of the WLM ecosystem.  
It transforms unstructured text into **dimensional knowledge structures** and then into  
**interpretable, deterministic knowledge graphs**.

This is the **fifth major layer** of WLM:

1. SLP‑World‑Interpreter — Language → Structure  
2. WLM‑World‑Model‑Interpreter — World Model → Structure  
3. WLM‑Agent‑Behavior — Structure → Behavior  
4. WLM‑Persona‑Engine — Structure → Identity  
5. **WLM‑Knowledge‑Engine — Structure → Knowledge**

It provides the missing link between **text** and **true understanding**:

> **Structure → Knowledge → Reasoning → World**

---

## Why this exists

LLMs do not understand knowledge.  
They interpolate token patterns and memorize embeddings.

This leads to:

- hallucinations  
- contradictions  
- shallow reasoning  
- no causal grounding  
- no temporal consistency  
- no spatial structure  

The WLM‑Knowledge‑Engine solves this by converting text into:

- dimensional structures  
- entity graphs  
- causal relations  
- temporal sequences  
- physical constraints  
- reasoning‑ready knowledge graphs  

This is **knowledge as structure**, not as embeddings.

---

## What this engine does

Given raw text, it produces:

- **entities**  
- **relations**  
- **dimensional annotations**  
- **tensions** (contradictions, missing links)  
- **closures** (future knowledge states)  

The output is a deterministic **KnowledgeGraph** object.

---

## Architecture

```
Text
  ↓
Extractor
  ↓
Dimension Engine
  ↓
Graph Builder
  ↓
Tension Detector
  ↓
Closure Predictor
  ↓
KnowledgeGraph
```

Each module is isolated, testable, and extensible.

---

## Design principles

- **Deterministic** — same text → same graph  
- **Interpretable** — explicit entities and relations  
- **Modular** — each engine evolves independently  
- **Dimension‑aligned** — grounded in spatial/temporal/physical/causal structure  
- **Expandable** — supports richer semantics in future phases  

---

## Status

MVP architecture complete.  
Dimensional reasoning and causal inference planned for Phase 2.

See `docs/roadmap.md` for upcoming milestones.
