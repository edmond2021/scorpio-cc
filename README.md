# scorpio-cc

A tiny, dependency-free **passphrase generator** written in Python.

It builds memorable, high-entropy passphrases by joining random words from a
built-in list, using the operating system's cryptographic random source
(`secrets`). No third-party dependencies, no network access, no data collected.

## Usage

```bash
# 4-word passphrase (default)
python passphrase.py
# -> bright-canyon-velvet-otter

# 5 words, custom separator, capitalized
python passphrase.py --words 5 --sep . --capitalize
# -> Maple.River.Indigo.Sage.Comet

# generate several at once
python passphrase.py --count 3
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `-w`, `--words` | number of words | `4` |
| `-s`, `--sep` | separator between words | `-` |
| `-c`, `--capitalize` | capitalize each word | off |
| `-n`, `--count` | how many passphrases to print | `1` |

## Why passphrases?

A handful of random common words is both easier to remember and harder to
brute-force than a short cryptic password. With an 83-word list, each word
adds about 6.4 bits of entropy, so a 4-word phrase is ~26 bits and a 6-word
phrase ~38 bits. (Use a larger word list for serious use — this is a demo.)

## Tests

```bash
python -m pytest          # if pytest is installed
python test_passphrase.py # or run the bundled runner directly
```

## License

Released under the [MIT License](LICENSE).
