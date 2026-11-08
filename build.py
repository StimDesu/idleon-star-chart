"""Builds index.html from src/template.html, src/stars.json and src/sample.json."""
import json, pathlib
root = pathlib.Path(__file__).parent
t = (root / "src/template.html").read_text(encoding="utf-8")
stars = json.loads((root / "src/stars.json").read_text(encoding="utf-8"))
sample = json.loads((root / "src/sample.json").read_text(encoding="utf-8"))
out = t.replace("__DATA__", json.dumps(stars, ensure_ascii=False)).replace("__SAMPLE__", json.dumps(sample, ensure_ascii=False))
(root / "index.html").write_text(out, encoding="utf-8")
print(f"index.html: {len(stars)} constellations, {sum(s['pts'] for s in stars)} points")
