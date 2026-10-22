#!/usr/bin/env python3
"""Translate Ook! source to Brainfuck using David Morgan-Mar's instruction map."""

import argparse
from pathlib import Path
import re
import sys

COMMANDS = {
    (".", "?"): ">",
    ("?", "."): "<",
    (".", "."): "+",
    ("!", "!"): "-",
    (".", "!"): ",",
    ("!", "."): ".",
    ("!", "?"): "[",
    ("?", "!"): "]",
    ("?", "?"): "",  # Give the memory pointer a banana (no operation).
}


def translate(source):
    if re.sub(r"Ook[.!?]|\s+", "", source):
        raise ValueError("source contains text other than Ook! tokens")
    tokens = re.findall(r"Ook([.!?])", source)
    if len(tokens) % 2:
        raise ValueError("Ook! requires an even number of tokens")
    commands = []
    depth = 0
    for index in range(0, len(tokens), 2):
        command = COMMANDS[tuple(tokens[index:index + 2])]
        if command == "[":
            depth += 1
        elif command == "]":
            depth -= 1
            if depth < 0:
                raise ValueError("closing loop has no matching opening loop")
        commands.append(command)
    if depth:
        raise ValueError("opening loop has no matching closing loop")
    return "".join(commands)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Ook! source file")
    args = parser.parse_args()
    try:
        result = translate(args.source.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        parser.exit(1, f"error: {error}\n")
    sys.stdout.write(result + "\n")


if __name__ == "__main__":
    main()
