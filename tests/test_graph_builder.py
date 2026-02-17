import pytest
from wlm_knowledge_engine.graph_builder import build_graph


def test_graph_builder_basic():
    entities = ["Earth", "Sun"]
    relations = []
    dims = {"spatial": {}, "temporal": {}, "physical": {}, "causal": {}}

    graph = build_graph(entities, relations, dims)

    assert graph["entities"] == entities
    assert graph["relations"] == relations
    assert graph["dimensions"] == dims
