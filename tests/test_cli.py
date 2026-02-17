import json
import subprocess
import sys
from pathlib import Path


def test_cli_extract(tmp_path):
    input_text = "The Earth orbits the Sun."
    input_file = tmp_path / "input.txt"
    input_file.write_text(input_text)

    result = subprocess.run(
        [sys.executable, "-m", "wlm_knowledge_engine.cli", "extract", str(input_file)],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0

    output = json.loads(result.stdout)
    assert "Earth" in output["entities"]
    assert "Sun" in output["entities"]
