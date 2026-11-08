"""Builds index.html from src/template.html, src/stars.json, src/areas.json and src/sample.json."""
import json, pathlib
root = pathlib.Path(__file__).parent
read = lambda p: json.loads((root / p).read_text(encoding="utf-8"))
t = (root / "src/template.html").read_text(encoding="utf-8")
stars, areas, sample = read("src/stars.json"), read("src/areas.json"), read("src/sample.json")
for s in stars:
    s["area"] = areas["stars"].get(s["id"], {})
dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))
out = t.replace("__DATA__", dump(stars)).replace("__SAMPLE__", dump(sample)).replace("__DOTS__", dump(areas["worlds"]))
(root / "index.html").write_text(out, encoding="utf-8")
print(f"index.html: {len(stars)} constellations, {sum(s['pts'] for s in stars)} points, "
      f"{sum(1 for s in stars if s['area'].get('w'))} with a world map")
