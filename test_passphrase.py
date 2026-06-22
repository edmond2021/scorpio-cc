"""Tests for passphrase.py — run with: python -m pytest  (or python test_passphrase.py)."""

import passphrase


def test_default_word_count():
    phrase = passphrase.generate()
    assert phrase.count("-") == 3  # 4 words -> 3 separators


def test_custom_word_count_and_separator():
    phrase = passphrase.generate(num_words=6, separator="_")
    assert phrase.count("_") == 5
    assert len(phrase.split("_")) == 6


def test_words_come_from_vocabulary():
    phrase = passphrase.generate(num_words=10)
    for word in phrase.split("-"):
        assert word in passphrase.WORDS


def test_capitalize():
    phrase = passphrase.generate(num_words=3, capitalize=True)
    for word in phrase.split("-"):
        assert word[0].isupper()


def test_invalid_count_raises():
    try:
        passphrase.generate(num_words=0)
    except ValueError:
        return
    raise AssertionError("expected ValueError for num_words=0")


def test_entropy_increases_with_words():
    assert passphrase.entropy_bits(6) > passphrase.entropy_bits(3)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"ok  {name}")
    print("All tests passed.")
