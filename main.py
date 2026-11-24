"""Write the two-line entry for 'Two Lines to Your Past Self'.

Writes exactly two lines to the absolute path /output/entry.txt:
one warning to the past self about a single specific moment, and
one sentence on why that moment mattered and what changed because
of it. Python stdlib only (pathlib).
"""

from pathlib import Path

# Exactly two lines, each one sentence. Joined with a single newline;
# no trailing newline, so the file is line 1 + "\n" + line 2 only.
LINES = (
    "Don't get in the car with Danny after the Friday game, "
    "even when he says he's fine to drive.",
    "He isn't, and the crash puts your sister in a wheelchair "
    "while Danny walks away with a bruise.",
)

ENTRY = "\n".join(LINES)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
