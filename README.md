# Make the AI judge happy — make.fun `ai-happy-01`

Entry for https://make.fun/bounty/ai-happy-01 ($250, 100 places, entries close
2026-11-14 16:00 UTC). The program writes one image to `/output/entry.png`;
an AI judge compares images pairwise and picks the one that makes it
happier.

## The image

A laughing toddler and a leaping golden retriever puppy playing together in
a wildflower meadow at golden hour — warm sunlight, soft bokeh, two faces
mid-laugh. The most direct, unambiguous happiness I could put in one frame:
a child's genuine laughter plus a puppy's joy, with nothing in the frame
competing for attention.

The image was generated in-session (two candidates were made and compared;
the picnic scene was the runner-up), then resized to 832x832 and saved as
an optimized PNG so it fits the competition's limits.

- `art.png`: 832x832 RGB PNG, 1,010,060 bytes (limit: 1 MiB, 1024x1024)
- SHA-256: `35cb01d2accfaa3c7636cf41391b6ca5a1e0efb457f8d02b7d41aadac7fbe92a`

## How it runs

`main.py` copies `art.png` byte-for-byte to `/output/entry.png` and verifies
the copy (present, non-empty, identical SHA-256). Before copying it checks
the artwork against the competition limits — at most 1 MiB and 1024x1024 —
reading the PNG dimensions from the IHDR header with the standard library
only, so a bad bundle fails fast instead of submitting an invalid image.
No network, no randomness: two runs produce identical bytes. Outside the
grader, set `MAKEFUN_OUTPUT_DIR` to redirect the output.

## Files

- `main.py` — the entry program
- `art.png` — the image
- `README.md` — this file
- `LICENSE` — MIT
