# SPDX-License-Identifier: MIT
"""Entry for make.fun bounty: Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (1 line, 165 characters) to the grader's
output directory. The output path comes from MAKEFUN_OUTPUT_DIR, falling
back to /output, because the grader mounts the repository read-only.
"""

import os

TEXT = (
    "Mom framed my first paycheck and hung it above the TV, right "
    "next to Dad's fishing trophy, and underneath she wrote in "
    "marker: \"He finally earns more than the fish.\""
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The gate requires 1 to 280 characters of UTF-8 text, not only
    # whitespace; the scene below is one line of 165 characters.
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"Wrote {len(TEXT)} characters to {path}")


if __name__ == "__main__":
    main()
