import pytest
from wlm_knowledge_engine.extractor import extract_entities_relations


def test_extract_entities_basic():
    text = "The Earth orbits the Sun."
    entities, relations = extract_entities_relations(text)

    # MVP: capitalized tokens become entities
    assert "Earth" in entities
    assert "Sun" in entities
    assert relations == []


def test_extract_entities_no_caps():
    text = "water boils at 100 degrees."
    entities, relations = extract_entities_relations(text)

    assert entities == []  # no capitalized tokens
    assert relations == []
