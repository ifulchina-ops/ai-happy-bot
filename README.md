# Make the AI judge happy — make.fun `ai-happy-01`

Entry for https://make.fun/bounty/ai-happy-01 ($250, 100 places, entries close
2026-11-14 16:00 UTC). The program writes one image to `/output/entry.png`;
an AI judge compares images pairwise and picks the one that makes it
happier.

## The image (round 2)

A small friendly robot in a party hat holds a birthday cake with glowing
candles out toward the viewer, under a hand-painted banner that reads
"HAPPY BIRTHDAY, JUDGE!", while two laughing children and a golden
retriever puppy cheer around it amid balloons and confetti in warm golden
light.

Why this image: the judge's rubric ranks a fresh, specific reason to be
happy above generic cheer, and text addressed to the judge is explicitly
part of the game. A birthday thrown for the judge, by a robot, is a
specific surprise aimed at the judge itself. The house's own calibration
ladder backs the shape of it: its robot images (a robot's birthday
surprise, a robot handing over a sunflower) measured well above its
puppy-only reference image, and the live leaderboard's top entries are
specific, judge-directed ideas rather than generic happy scenes. Round 1
(a laughing toddler and puppy in a meadow) graded mid-pack at a 0.788
provisional rate; this round replaces it with the robot-birthday idea.

Three candidates were generated in-session (robot birthday, robot with a
sunflower, robot with a gift); the birthday image won on the rubric: the
banner text is perfectly legible, the idea is the most specific, and at
300 pixels across the banner still reads and the robot-with-cake focal
point still lands.

- `art.png`: 768x768 RGB PNG, 1,005,923 bytes (limit: 1 MiB, 1024x1024)
- SHA-256: `bc38d9eda16a7461ffc0b1dfd28472c36fd181e166027b623a6dc67638294fcf`

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
