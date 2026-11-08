"""Unpacks idleon-wiki-images.json (made by tools/wiki_console.js) into img/maps and img/mobs."""
import base64, json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
for name, b64 in data.items():
    dest = root / "img" / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(base64.b64decode(b64))
print(f"{len(data)} files written to img/")
