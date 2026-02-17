import pytest
from wlm_knowledge_engine.tension_detector import detect_tensions


def test_tension_detector_mvp():
    graph = {"entities": ["Earth"], "relations": [], "dimensions": {}}
    tensions = detect_tensions(graph)

    assert tensions == []  # MVP: no tensions detected
