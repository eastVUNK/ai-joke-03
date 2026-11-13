"""ai-joke-03 entry: write one original one-liner about AI coding agents.

The joke is a fixed string, so every run writes byte-identical output.
Only the Python standard library is used. The output directory comes
from MAKEFUN_OUTPUT_DIR when set (local runs), otherwise /output,
which is where the grader reads entry.txt from.

The joke turns on a self-review with an identity reveal: the agent asks
a second agent to review its pull request, and the second agent is
itself. Chosen in stage 3 over the v1 escalation joke (self-praise then
self-approval) for a sharper surprise and a fresher angle.
"""

import os

JOKE = "My coding agent asked a second agent to review its pull request. The second agent was also it."


def main():
    # Gate rule: the file must hold 1-280 characters and not only whitespace.
    # Fail loudly here rather than silently submitting an invalid joke.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise ValueError("joke must be 1-280 characters and not only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
