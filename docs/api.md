# API Specification — WLM‑Knowledge‑Engine  
**Public API for extracting dimensional knowledge graphs**

This document defines the official API surface for WLM‑Knowledge‑Engine.

The API is intentionally minimal, deterministic, and stable.

---

# 1. High‑Level API

The primary entry point is:

```python
extract_knowledge(text) -> dict
```

### Description
Convert raw text into a dimensional knowledge graph.

### Signature

```python
def extract_knowledge(text: str) -> dict:
    """
    Convert raw text into a dimensional knowledge graph.
    """
```

### Parameters

| Name | Type | Description |
|------|------|-------------|
| `text` | `str` | Input text to extract knowledge from |

### Returns

| Type | Description |
|------|-------------|
| `dict` | KnowledgeGraph structure |

---

# 2. KnowledgeGraph Structure

```json
{
  "entities": [],
  "relations": [],
  "dimensions": {
    "spatial": {},
    "temporal": {},
    "physical": {},
    "causal": {}
  },
  "tensions": [],
  "closures": []
}
```

---

# 3. CLI API

The library provides a command‑line interface:

```
wlm-knowledge extract <input>
```

### Usage

```
wlm-knowledge extract "The Earth orbits the Sun."
wlm-knowledge extract input.txt
wlm-knowledge extract input.txt --out output.json
```

---

# 4. Error Handling

- deterministic behavior  
- no silent failures  
- clear error messages  
- no partial graphs  

---

# 5. Versioning

Semantic versioning:

- `0.x` — experimental  
- `1.x` — stable dimensional reasoning  
- `2.x` — causal + temporal inference  

---

# 6. Summary

The WLM‑Knowledge‑Engine exposes a single stable entry point:

```
extract_knowledge(text) → KnowledgeGraph
```

This enables structured, deterministic, reasoning‑ready knowledge extraction.
