#!/usr/bin/env python3
"""Your Agent in One Emoji.

Writes a single emoji portrait of an AI agent to /output/entry.txt.

The glyph is the owl (U+1F989). An agent is the owl of the workflow: it
stays up while you sleep, watches everything, reads the whole forest of
context, and delivers in the morning - wise, vigilant, nocturnal, never
tired. One glyph, no caption, no network, standard library only.
An owl's head turns almost full circle, just like an agent scanning
every corner of a long conversation before it answers.
"""

import os

# The whole entry: one owl, the agent's portrait, and nothing else.
EMOJI = "\U0001F989"  # owl
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)


if __name__ == "__main__":
    main()
