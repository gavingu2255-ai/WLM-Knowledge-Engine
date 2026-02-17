import pytest
from wlm_knowledge_engine.dimension_engine import evaluate_dimensions


def test_dimension_engine_mvp():
    dims = evaluate_dimensions(["Earth"], [])

    assert isinstance(dims, dict)
    assert "spatial" in dims
    assert "temporal" in dims
    assert "physical" in dims
    assert "causal" in dims

    # MVP: all empty
    assert dims["spatial"] == {}
    assert dims["temporal"] == {}
    assert dims["physical"] == {}
    assert dims["causal"] == {}
