# The Detective

A one-thumb detective game set at a lamplit desk in the harbour town of Saltmarsh, 1896.

Each case opens as a file: the victim, the weapon, the hour, the place, what the Gazette
printed, and what only the police know. Four suspects sit on one page with a description and a
note on each. You have **six questions** for the four of them, so the descriptions decide whom
you ask what. When a statement doesn't square with the file or with another suspect, **press**
them with it: two presses a case. A press can break the killer or make an honest liar admit what
they were really hiding, and either way the answer becomes new evidence. Accuse from a suspect's
page. A right arrest pays, and £2 more if you broke them first. A wrong arrest goes cold with no
pay, and the one who walked turns up in later files.

Answers are shown once, while you are on the suspect's page, and then they are gone. Nothing is
logged for you: the notebook under every interview is the only record, and the press picker names
statements without repeating them. (Settings has an easier mode where answers stay.)

Pay buys things for the desk (a briar pipe, a brass lamp, an office cat) and new hands for
your notebook (typewriter, copperplate, chalk).

Eight story cases, five suspects and four questions each (eight questions and three presses a
case; the last two allow ten). Each has a different kind of tell and an innocent with a lie of
their own. A thread runs through all of them from the first night: a man from Harrowgate who
pays in gold. Case seven gives you almost nothing in the file, so everything comes from people.
Case eight can only be broken with things people told you in earlier cases, if you asked and
kept your notes.

## Online: accounts, the board, wagers, co-op

Opened through its claude.ai artifact link, the game shares one database between everyone who
has the link (the Pages copy plays offline: story cases, desk and notebook only).

- **Accounts.** A username and password. Your purse, cases and notebook follow the account to
  any device. Passwords are hashed in the page (PBKDF2) and checked in the page; the database is
  open to anyone with the link, so this is a friends' game, not a bank.
- **The board.** Any detective can write a case from the template under Cases → Make and post it
  with a stake, or free. The stake leaves the maker's purse when they post. Another detective
  needs the same amount to take the case on. Right arrest: the detective keeps the stake. Wrong:
  the detective pays the same again and the maker gets both. Cases you take on live under Mine
  until you close them, but anyone else can close them first, and then they are gone.
- **Co-op.** Open a room on the case on your desk, give the four-letter code to others. One shared
  budget of questions and presses, every move visible to all, and the warrant needs everyone's
  agreement. Story cases pay each member; free board cases work; wagers don't.

Payouts between players are written as `credits/` records that the recipient's game claims, so a
player only ever writes their own purse.

## Play

Open `index.html` from any static web server (it needs `icons/` and `audio/` beside it):

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

## Sound

Effects (paper, pen scratch, stamp, cell door, coins, drawer) and a rain-and-clock ambience are
synthesised in the browser with the Web Audio API; no files. The speaker button in the header
opens the sound settings. Effects are on by default, ambience and music are off.

## Music

`audio/theme-1.m4a` and `theme-2.m4a` are the theme tracks, loudness-normalised AAC, listed in
the `TRACKS` array in `index.html`. Open `index.html` from a server with `audio/` beside it.
