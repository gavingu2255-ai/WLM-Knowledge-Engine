# Example: Causal Chain  
**Text → Entities → (Future) Causal Structure**

This example shows how the engine handles a causal sentence.

---

## Input

```
Gravity causes objects to fall.
```

---

## Code

```python
from wlm_knowledge_engine import extract_knowledge

kg = extract_knowledge("Gravity causes objects to fall.")
print(kg)
```

---

## Output (MVP)

```
{
  "entities": ["Gravity"],
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

- **Entities** = `Gravity`  
- **Relations** = empty  
- **Dimensions** = empty  

Future versions will extract:

- causal relation: `causes(Gravity, falling)`  
- physical dimension: acceleration  
- closure: predicted motion  
