"""A small, dependency-free passphrase generator.

Generates memorable, high-entropy passphrases by joining random words
from a built-in word list, using the OS cryptographic RNG (secrets).

Example:
    $ python passphrase.py --words 5 --sep -
    bright-canyon-velvet-otter-mango

This is a self-contained demo project: standard library only, no privacy
or external data involved.
"""

from __future__ import annotations

import argparse
import math
import secrets

# A small curated word list (common, easy-to-read English words).
WORDS: list[str] = [
    "amber", "anchor", "apple", "arrow", "autumn", "basil", "bridge",
    "bright", "canyon", "cedar", "cliff", "clover", "cobalt", "comet",
    "coral", "cosmos", "cotton", "crisp", "delta", "ember", "fable",
    "falcon", "feather", "ferry", "forest", "garnet", "ginger", "glacier",
    "harbor", "hazel", "indigo", "island", "ivory", "jasmine", "jolly",
    "juniper", "kettle", "lagoon", "lantern", "lemon", "lilac", "lunar",
    "mango", "maple", "marble", "meadow", "mellow", "mint", "misty",
    "north", "nutmeg", "ocean", "olive", "onyx", "orbit", "otter",
    "pepper", "pine", "pixel", "plum", "polar", "quartz", "quiet",
    "raven", "ripple", "river", "robin", "saffron", "sage", "silver",
    "solar", "spruce", "summit", "sunny", "thistle", "tulip", "umber",
    "valley", "velvet", "vivid", "willow", "winter", "zephyr",
]


def generate(num_words: int = 4, separator: str = "-", capitalize: bool = False) -> str:
    """Return a passphrase made of `num_words` random words."""
    if num_words < 1:
        raise ValueError("num_words must be >= 1")
    chosen = [secrets.choice(WORDS) for _ in range(num_words)]
    if capitalize:
        chosen = [w.capitalize() for w in chosen]
    return separator.join(chosen)


def entropy_bits(num_words: int, vocabulary: int = len(WORDS)) -> float:
    """Approximate entropy in bits for a passphrase of `num_words` words."""
    return num_words * math.log2(vocabulary)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a memorable passphrase.")
    parser.add_argument("-w", "--words", type=int, default=4,
                        help="number of words (default: 4)")
    parser.add_argument("-s", "--sep", default="-",
                        help="separator between words (default: '-')")
    parser.add_argument("-c", "--capitalize", action="store_true",
                        help="capitalize each word")
    parser.add_argument("-n", "--count", type=int, default=1,
                        help="how many passphrases to generate (default: 1)")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    for _ in range(args.count):
        print(generate(args.words, args.sep, args.capitalize))
    bits = entropy_bits(args.words)
    print(f"# ~{bits:.0f} bits of entropy from a {len(WORDS)}-word list",
          flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
