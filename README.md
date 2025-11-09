# P0 — Text Cleaner (Beginner)

**What:** CSV in → cleaned CSV out (lowercase, emoji/punctuation removal, basic regex).  
**Why:** Beginner-friendly CLI showing Python, pandas, tests, and reproducibility.

## Run locally
1. python3 -m venv .venv && source .venv/bin/activate
2. pip install -r requirements.txt
3. python clean.py --in_csv data/sample.csv --out_csv data/out.csv --col text

## Tests
1. export PYTHONPATH=.
2. pytest -q

## Example (before → after)
| input             | output          |
|-------------------|-----------------|
| Hello, World! 😊  | hello world     |
| Grüße aus Köln!!! | grüße aus köln  |

## Files
- clean.py — cleaning function + CLI
- tests/test_clean.py — 2 basic tests
- data/sample.csv — sample input
- requirements.txt — dependencies

## Next
- Add flags: keep/remove emojis, custom regex
- Add a 90s demo video and pin this repo

## Flags
- `--keep-emoji`: keep emojis (default removes)
- `--keep-punct`: keep punctuation (default removes)
