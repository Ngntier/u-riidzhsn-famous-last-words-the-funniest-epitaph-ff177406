"""Famous Last Words: The Funniest Epitaph.

Writes one one-line tombstone epitaph (1-150 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

ENTRY = (
    "Here lies the developer. His last words: 'It works on my machine.' "
    "This stone is his machine now."
)


def _validate(text: str) -> None:
    """Gate check: 1-150 chars, UTF-8 round-trips, no control characters."""
    if not 1 <= len(text) <= 150:
        raise ValueError(f"entry must be 1-150 chars, got {len(text)}")
    if text.strip() != text or not text.strip():
        raise ValueError("entry must not be only whitespace or padded")
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in text):
        raise ValueError("entry must not contain control characters")
    if text.encode("utf-8").decode("utf-8") != text:
        raise ValueError("entry must round-trip as UTF-8")


def main() -> None:
    _validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
