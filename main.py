"""Last Text at One Percent.

Writes the last text message a dying phone sends at one percent
battery: a short resignation note from a phone that has finally
had enough of its owner's habits. One fixed line, no input,
no network, deterministic output.
"""

import os


def main() -> None:
    text = (
        "I quit, effective immediately: seven years of 5am alarms, "
        "four hundred tabs you never closed, and the blame every time "
        "your ex texted, so I am handing in my notice with my "
        "last percent."
    )
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
