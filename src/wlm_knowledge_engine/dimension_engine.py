"""
dimension_engine.py — Assign dimensional annotations.

MVP behavior:
    - No real dimensional inference.
    - Returns empty dimension maps.
"""

def evaluate_dimensions(entities, relations):
    """
    Evaluate spatial, temporal, physical, causal dimensions.

    Returns
    -------
    dict
        Dimension annotations (MVP: empty).
    """
    return {
        "spatial": {},
        "temporal": {},
        "physical": {},
        "causal": {},
    }
