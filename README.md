# IdleOn Star Chart

**Live page: https://stimdesu.github.io/idleon-star-chart/**

Paste your Legends of Idleon save and see every constellation (A-1 … F-9) in one compact table: which ones are complete, and for each character whether they are counted, can be counted with a single click, or still miss the requirement.

The page picks English or Russian from your browser language; the EN/RU switch in the corner overrides it.

## What the page shows

| Mark | Meaning |
|---|---|
| ✓ | the character is counted |
| ★ | requirement met (level, class, "reach this star"): walk up and click the star |
| ⇥ | requirement met (Trapping 15, Cooking 15): just enter the map |
| ? | AFK or a fight event, can't be checked from the save |
| × | requirement not met |
| · | the constellation is already complete |

A constellation only completes when someone clicks its star after enough characters are counted. The page flags those as "click to complete".

Hover or tap a star ID or a cell for the map, the exact star position, the original requirement text and the star chart points.

## How to get your save

Any raw save export with the `SSprog`, `Lv0_0`…`Lv0_N` and `CharacterClass_N` keys works, for example "Raw data" from IdleOn Efficiency. Both a flat export and `{ "data": {...}, "charNames": [...] }` are accepted. The save stays in your browser; nothing is uploaded.

## How it works

In the save, `SSprog[i] = [letters, complete]`. Each letter is a character slot: `_` is the first character, `a` the second, … `i` the tenth. Requirements, thresholds and point values come from the game's `StarQuests` list. Star positions are from [idleon.wiki/wiki/Star_Signs](https://idleon.wiki/wiki/Star_Signs).

## Building

`index.html` is generated. Edit the files in `src/` and run:

```
python build.py
```

Legends of Idleon belongs to Lavaflame2. This is an unofficial fan tool.
