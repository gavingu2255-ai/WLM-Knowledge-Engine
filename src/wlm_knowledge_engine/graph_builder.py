"""
graph_builder.py — Build a normalized knowledge graph.

MVP behavior:
    - Wraps entities, relations, and dimensions into a graph dict.
"""

def build_graph(entities, relations, dimensions):
    """
    Build a knowledge graph structure.

    Returns
    -------
    dict
        Graph structure.
    """
    return {
        "entities": list(entities),
        "relations": list(relations),
        "dimensions": dict(dimensions),
    }
