"""3 AM hardware wallet excuse entry: writes one line to OUTPUT_DIR/entry.txt (stdlib only, deterministic)."""
import os

ENTRY = "Sign at 3 AM? No. Nothing good has ever been confirmed after midnight. Ask your ex. Ask that dog coin."
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main():
    # Gate: UTF-8 text inside the bounty's character limit, not only white space.
    assert ENTRY.strip() and 1 <= len(ENTRY) < 200
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
