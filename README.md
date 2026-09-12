# The Detective

A one-thumb detective game set at a lamplit desk in the harbour town of Saltmarsh, 1896.

Each case opens as a file: the victim, the weapon, the hour, the place, what the Gazette
printed, and what only the police know. Four suspects sit on one page with a description
and a note on each. Ask each of them three questions. One of them will say something they
could not know, or could not have done. Accuse from their page. A right arrest pays; a wrong
one sends the case to the cold drawer with no pay.

Pay buys things for the desk (a briar pipe, a brass lamp, an office cat) and new hands for
your notebook (typewriter, copperplate, chalk). The notebook itself is yours to type in and
collects every statement you hear.

Six cases are written. Each has a different kind of tell: a detail the killer could not
have known, an alibi that contradicts the file, a register entry, a physical description.

## Play

Open `index.html` from any static web server (it needs `icons/` beside it):

```
python -m http.server 8766
```

then visit <http://localhost:8766/>. Progress, purse and notebook are saved in the browser.
On a phone, "Add to Home Screen" installs it with the detective icon.

## Single-file build

```
python build.py
```

writes `dist/index.html` with any `audio/` tracks inlined as data URIs, for hosts that
block external media.

## Structure

Everything lives in `index.html`. Cases, suspects, answers, decor and notebook hands are a
JSON block at the top of the file, so new cases are data, not code. `make_icons.py` redraws
the icon set in `icons/`; `manifest.json` makes it installable.

## Music

No tracks ship yet. Drop files in `audio/` and list them in the `TRACKS` array in
`index.html`; the ♪ button and desk music bar appear automatically, off by default.
