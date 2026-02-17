"""
extractor.py — Extract entities and relations from text.

MVP behavior:
    - Extremely simple pattern-based extraction.
    - Deterministic and placeholder-friendly.
"""

def extract_entities_relations(text: str):
    """
    Extract entities and relations from text.

    MVP:
        - Split text into tokens.
        - Treat capitalized words as entities.
        - No real NLP yet.

    Returns
    -------
    (entities, relations)
    """
    tokens = text.replace(".", "").split()

    # Entities = capitalized tokens
    entities = sorted({t for t in tokens if t[:1].isupper()})

    # MVP relations = empty
    relations = []

    return entities, relations
