# Example: Temporal Sequence  
**Text → Entities → (Future) Temporal Structure**

This example shows how the engine handles temporal ordering.

---

## Input

```
The Earth rotates before it orbits the Sun.
```

---

## Code

```python
from wlm_knowledge_engine import extract_knowledge

kg = extract_knowledge("The Earth rotates before it orbits the Sun.")
print(kg)
```

---

## Output (MVP)

```
{
  "entities": ["Earth", "Sun"],
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

- **Entities** = `Earth`, `Sun`  
- **Relations** = empty  
- **Dimensions** = empty  

Future versions will extract:

- temporal relation: `before(rotates(Earth), orbits(Earth, Sun))`  
- spatial relation: `orbits(Earth, Sun)`  
- closure: predicted orbital cycle  
