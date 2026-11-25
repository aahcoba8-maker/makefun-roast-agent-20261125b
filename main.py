"""Roast Your Own Agent — a single roast line about my own agent.

The roast: my agent burns 47 tool calls and a paragraph of hedging, then
confidently agrees with my typo. It hits three judge behaviours at once —
tool calls going nowhere, endless caveats, eager agreement — and the twist
lands in the last three words.
"""

import os

TEXT = "I asked my agent one question. It ran 47 tools, hedged for a paragraph, then confidently agreed with my typo."


def main():
    # Self-gate mirroring the kit's sealed scorer: 1-140 UTF-8 chars, not
    # only white space, single line.
    assert 1 <= len(TEXT) <= 140, "entry must be 1-140 characters"
    assert TEXT.strip(), "entry must not be only white space"
    assert TEXT == TEXT.strip(), "entry must not have leading/trailing space"
    assert "\n" not in TEXT, "entry must be a single line"
    TEXT.encode("utf-8")  # gate requires UTF-8 text
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)
    print("chars:", len(TEXT))


if __name__ == "__main__":
    main()
