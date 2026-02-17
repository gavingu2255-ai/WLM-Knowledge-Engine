"""
Command-line interface for WLM‑Knowledge‑Engine.

Usage:
    wlm-knowledge extract "The Earth orbits the Sun."
    wlm-knowledge extract input.txt
"""

import argparse
import json
import sys
from pathlib import Path

from .api import extract_knowledge


def load_input(input_arg: str):
    """
    Load input either from a text file or inline string.
    """
    path = Path(input_arg)
    if path.exists() and path.is_file():
        return path.read_text(encoding="utf-8")
    return input_arg


def cmd_extract(args):
    try:
        text = load_input(args.input)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    kg = extract_knowledge(text)

    if args.out:
        Path(args.out).write_text(json.dumps(kg, indent=2), encoding="utf-8")
    else:
        print(json.dumps(kg, indent=2))


def main():
    parser = argparse.ArgumentParser(
        prog="wlm-knowledge",
        description="WLM‑Knowledge‑Engine CLI"
    )

    sub = parser.add_subparsers(dest="command")

    # extract
    p_extract = sub.add_parser(
        "extract",
        help="Extract a knowledge graph from text"
    )
    p_extract.add_argument("input", help="Text file path or inline text")
    p_extract.add_argument("--out", help="Write output to file")
    p_extract.set_defaults(func=cmd_extract)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(1)

    args.func(args)
