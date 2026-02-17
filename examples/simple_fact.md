# Example: Simple Fact  
**Text → Entities → Knowledge Graph**

This example shows how the engine extracts entities from a simple factual sentence.

---

## Input

```
Water boils at 100°C.
```

---

## Code

```python
from wlm_knowledge_engine import extract_knowledge

kg = extract_knowledge("Water boils at 100°C.")
print(kg)
```

---

## Output (MVP)

```
{
  "entities": ["Water"],
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

## Explanation

In the MVP:

- **Entities** = capitalized tokens → `Water`  
- **Relations** = not extracted yet  
- **Dimensions** = empty  
- **Tensions / Closures** = empty  

Future versions will extract:

- physical relation: `boils_at(Water, 100°C)`  
- physical dimension: temperature threshold  
