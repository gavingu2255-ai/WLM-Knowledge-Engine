import pytest
from wlm_knowledge_engine.closure_predictor import predict_closures


def test_closure_predictor_mvp():
    graph = {"entities": ["Earth"], "relations": [], "dimensions": {}}
    closures = predict_closures(graph)

    assert closures == []  # MVP: no closures predicted
