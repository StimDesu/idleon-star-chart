# Images from the IdleOn MMO Wiki

- `A-1.png` … `F-9.png`: constellation location screenshots
- `maps/w1.png` … `maps/w6.png`: world area maps
- `mobs/*.gif`: idle animations of the monsters on each map

All of them come from the IdleOn MMO Wiki
([Star Signs](https://idleon.wiki/wiki/Star_Signs),
[Constellation Locations](https://idleon.wiki/wiki/Constellation_Locations),
[Worlds](https://idleon.wiki/wiki/Worlds)).

They are licensed under [Creative Commons Attribution-NonCommercial 3.0](https://creativecommons.org/licenses/by-nc/3.0/)
by the IdleOn MMO Wiki contributors, not under this repository's MIT license.
They are used here unchanged, in a non-commercial fan tool. The game art in them
belongs to Lavaflame2.

To download them again: `python tools/fetch_wiki_images.py`. If the wiki's CDN is
too slow for scripts, paste `tools/wiki_console.js` into the browser console on
any idleon.wiki page, then run `python tools/unpack_wiki_images.py idleon-wiki-images.json`
and `python tools/fetch_wiki_images.py` (it skips files that exist and writes
`src/areas.json`).
