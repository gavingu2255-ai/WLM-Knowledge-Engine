import pytest
from wlm_knowledge_engine.api import extract_knowledge


def test_end_to_end_extraction():
    text = "The Earth orbits the Sun."

    kg = extract_knowledge(text)

    assert "Earth" in kg["entities"]
    assert "Sun" in kg["entities"]

    # MVP: relations empty
    assert kg["relations"] == []

    # Dimensions exist
    assert "spatial" in kg["dimensions"]
    assert "temporal" in kg["dimensions"]
    assert "physical" in kg["dimensions"]
    assert "causal" in kg["dimensions"]

    # MVP: no tensions or closures
    assert kg["tensions"] == []
    assert kg["closures"] == []
