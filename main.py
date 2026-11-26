# SPDX-License-Identifier: MIT
"""Entry for make.fun bounty: Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (1 line, 161 characters) to the grader's
output directory. The output path comes from MAKEFUN_OUTPUT_DIR, falling
back to /output, because the grader mounts the repository read-only.
"""

import os

TEXT = (
    "I taught my grandmother to video-call, and her first call was "
    "to the neighbour — to tell her, live on camera, that her cat "
    "had been stealing our fish for a year."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The gate requires 1 to 280 characters of UTF-8 text, not only
    # whitespace; the scene below is one line of 161 characters.
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"Wrote {len(TEXT)} characters to {path}")


if __name__ == "__main__":
    main()
