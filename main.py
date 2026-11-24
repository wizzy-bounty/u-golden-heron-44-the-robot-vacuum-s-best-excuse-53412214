"""The Robot Vacuum's Best Excuse.

Writes one line, at most 140 characters: the funniest excuse a robot
vacuum gives for missing a spot. Deterministic, stdlib only, no network.
"""

import os

LINE = "My bumper tapped the chair leg 47 times. It never apologized, so I left its dust as a warning."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
