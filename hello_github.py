#!/usr/bin/env python3
"""A tiny starter script for this repository."""

import argparse
from datetime import date


def greeting(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a friendly GitHub greeting.")
    parser.add_argument("--name", default="GitHub", help="Name to greet")
    args = parser.parse_args()

    print(greeting(args.name))
    print(f"Date: {date.today().isoformat()}")


if __name__ == "__main__":
    main()
