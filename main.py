# SPDX-License-Identifier: MIT
"""Entry for make.fun bounty: Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (1 line, 166 characters) to the grader's
output directory. The scene: a son asks Dad to check under his bed for
monsters, and the monster has already moved into the closet because Dad
is scarier. The output path comes from MAKEFUN_OUTPUT_DIR, falling
back to /output, because the grader mounts the repository read-only.
"""

import os

TEXT = "My son asked me to check under his bed for monsters, so I checked, and the monster, he said, had already moved into the closet, because 'you're scarier than me, Dad.'"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The gate requires 1 to 280 characters of UTF-8 text, not only
    # whitespace; the scene below is one line of 166 characters.
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"Wrote {len(TEXT)} characters to {path}")


if __name__ == "__main__":
    main()
