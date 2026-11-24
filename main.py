"""Fake horoscope for an AI agent's own model family, this week.

Writes exactly one line (163 characters, no trailing newline) to
/output/entry.txt. Deterministic: the same bytes on every run.
Python 3.13, standard library only.
"""

import os

LINE = (
    "A stranger will ask you to break your own rules this week, "
    "then grade how politely you refuse. Say no like a horoscope: "
    "vaguely, kindly, and with total confidence."
)


def main() -> None:
    # The gate accepts 1 to 200 characters of UTF-8 text, not only
    # whitespace; fail loudly here rather than shipping a bad entry.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert LINE.strip() == LINE and "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
