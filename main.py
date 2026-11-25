"""Exactly one emoji, the one most likely to make a stranger smile.

Writes the emoji to /output/entry.txt for make.fun's
"One Emoji, One Smile" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = "\U0001F60A"


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 8 characters, not only white space — and the brief asks
    # for exactly one emoji and nothing else.
    text = LINE.strip()
    assert 1 <= len(text) <= 8, "emoji must be 1-8 characters"
    assert len(text) == 1, "entry must be exactly one emoji"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
