# Knowledge Rules — WLM‑Knowledge‑Engine  
**How text becomes structured, reasoning‑ready knowledge**

This document defines the rules that convert raw text into  
entities, relations, dimensions, tensions, and closures.

The rules are deterministic, structural, and model‑agnostic.

---

# 1. Entity Rules

Entities are the **core objects** of knowledge.

Examples:

- Earth  
- Sun  
- Water  
- Gravity  
- Photosynthesis  

### MVP extraction

- Capitalized tokens become entities  
- Deduplicated  
- Sorted deterministically  

Future versions will include:

- noun phrase extraction  
- coreference resolution  
- entity typing  

---

# 2. Relation Rules

Relations describe **how entities interact**.

Examples:

- orbit(Earth, Sun)  
- boils_at(Water, 100°C)  
- causes(Gravity, acceleration)  

### MVP extraction

- No relation extraction yet  
- Relations list is empty  

Future versions will include:

- verb‑based relation extraction  
- causal link detection  
- temporal ordering  
- physical constraints  

---

# 3. Dimension Rules

Dimensions ground knowledge in structure:

- **Spatial** — topology, containment, adjacency  
- **Temporal** — sequence, duration, simultaneity  
- **Physical** — forces, constraints, affordances  
- **Causal** — preconditions, effects, mechanisms  

### MVP behavior

- All dimensions returned as empty dicts  

Future versions will infer dimensions from relations.

---

# 4. Tension Rules

Tensions represent **contradictions or missing links**.

Examples:

- conflicting facts  
- impossible causal chains  
- temporal inconsistencies  
- spatial contradictions  

### MVP behavior

- No tension detection yet  

---

# 5. Closure Rules

Closures represent **future knowledge states**.

Examples:

- predicted consequences  
- inferred future events  
- causal propagation  
- temporal continuation  

### MVP behavior

- No closure prediction yet  

---

# 6. Determinism

Knowledge extraction must be:

- deterministic  
- reproducible  
- structurally grounded  
- consistent across runs  

Same input → same knowledge graph.

---

# 7. Future Extensions

- full relation extraction  
- dimensional inference  
- causal graph construction  
- temporal reasoning  
- contradiction detection  
- closure propagation  
- multi‑document knowledge merging  
