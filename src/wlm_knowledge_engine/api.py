"""
High‑level API for WLM‑Knowledge‑Engine.

This module exposes a single entry point:

    extract_knowledge(text) -> KnowledgeGraph

MVP behavior:
    - Returns a deterministic knowledge graph structure.
"""

from .extractor import extract_entities_relations
from .dimension_engine import evaluate_dimensions
from .graph_builder import build_graph
from .tension_detector import detect_tensions
from .closure_predictor import predict_closures


def extract_knowledge(text: str) -> dict:
    """
    Convert raw text into a dimensional knowledge graph.

    Parameters
    ----------
    text : str
        Input text.

    Returns
    -------
    dict
        KnowledgeGraph structure.
    """
    entities, relations = extract_entities_relations(text)
    dimensions = evaluate_dimensions(entities, relations)
    graph = build_graph(entities, relations, dimensions)
    tensions = detect_tensions(graph)
    closures = predict_closures(graph)

    return {
        "entities": entities,
        "relations": relations,
        "dimensions": dimensions,
        "tensions": tensions,
        "closures": closures,
    }
