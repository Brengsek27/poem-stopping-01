"""Write a fixed poem to the output directory.

The program validates the poem length, writes it as UTF-8 to
entry.txt inside the directory given by the MAKEFUN_OUTPUT_DIR
environment variable or /output by default, and reports how many
Unicode code points and bytes were written.
"""

import os
import sys
# The poem is fixed; validation guards its published length.
def _code_points(text: str) -> int:
    return len(text)

POEM = (
    "The gardener could prune one more branch, chase one more weed.\n"
    "Instead she sets the shears in the grass\n"
    "and watches the garden be a garden.\n"
    "Her hands are empty.\n"
    "Nothing she loves is escaping."
)


def main() -> None:
    cp = len(POEM)
    if not (1 <= cp <= 280):
        raise ValueError(f"Poem must be between 1 and 280 code points (got {cp})")
    if POEM.strip() == "":
        raise ValueError("Poem cannot be only whitespace")
    out_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = POEM.encode("utf-8")
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)
    print(f"{cp} code points, {len(data)} bytes written")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.exit(str(e))
