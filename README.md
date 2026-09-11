# Dead Letter

A one-thumb mobile mystery. You are the night clerk at a harbour town's Dead Letter Office.
Letters nobody could deliver land on your desk: read them, tap the words that are clues,
find the right door on the map. Deliver it right and a reply comes with the morning.
Deliver it wrong and it bounces back, and the town talks.

Two districts are written:

- **The Docks** — twelve letters, a drowned boat that isn't, a man three streets from his widow.
- **The Old Quarter** — twelve letters, a clock stopped since 1871, a solicitor's ledgers,
  and a magnifying glass for rain-faded ink.

## Play

Open `index.html` from any static web server (it needs `audio/` beside it for the music).
Locally:

```
python -m http.server 8766
```

then visit <http://localhost:8766/>. Progress and your notebook are saved in the browser.

## Single-file build

```
python build.py
```

writes `dist/index.html` with the five music tracks inlined as data URIs, for hosts that
block external media.

## Structure

Everything lives in `index.html`. Game content (districts, streets, buildings, directory,
census cards, letters, replies) is a JSON block at the top of the file, so new letters and
districts are data, not code. Faded words are marked `⟦like this⟧` and need the glass.
Letters with a `keep` array are addressed to the clerk and offer a choice instead of a door.

## Music

`audio/theme-1..5.m4a` are the theme tracks (64 kbps AAC). The player cycles through them;
the ♪ button in the header and the bar at the bottom of the desk control it.
