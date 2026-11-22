#!/usr/bin/env python3
"""Write a short text that relaxes its reader to /output/entry.txt.

The text is a quiet room after the last guest has left: warm chairs,
a glass of water holding the afternoon in one circle of light, and no
one waiting for an answer. It shows the calm instead of instructing it.

The file holds exactly the text (273 code points, no trailing newline),
so the gate counts what the reader reads and nothing else.
"""

import os

TEXT = (
    "Somewhere a room has gone quiet after the last guest left. "
    "The chairs are still warm. "
    "On the table, a glass of water holds the afternoon in one circle "
    "of light, and it is not going anywhere. "
    "No one is waiting for an answer from you here. "
    "You can stay while the light lasts."
)


def main() -> None:
    # The gate counts the file as Unicode code points: 1 to 280, and not
    # only whitespace. Fail loudly instead of writing an invalid entry.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError(f"entry text is {len(TEXT)} code points")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
