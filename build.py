"""Bundle index.html into dist/index.html with the audio inlined as data URIs.

The repo version references audio/theme-N.m4a so it plays from GitHub Pages or any
static host. The bundled version is a single file for hosts that block external media
(for example the claude.ai artifact sandbox). The artifact uses the claude.ai runtime
for online play, so the Firestore config tag is dropped from the bundle.
"""
import base64, pathlib, re

root = pathlib.Path(__file__).parent
src = (root / "index.html").read_text(encoding="utf-8")

def inline(m):
    p = root / m.group(0)
    b64 = base64.b64encode(p.read_bytes()).decode("ascii")
    return f"data:audio/mp4;base64,{b64}"

out = re.sub(r"audio/theme-\d+\.m4a", inline, src)
out = out.replace('<script src="firebase-config.js"></script>\n', '')
dist = root / "dist"
dist.mkdir(exist_ok=True)
(dist / "index.html").write_text(out, encoding="utf-8")
print(f"wrote dist/index.html ({len(out)/1e6:.1f} MB)")
