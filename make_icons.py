"""Draw the detective silhouette app icon (fedora, popped collar, coat) as PNGs and an SVG."""
from PIL import Image, ImageDraw
import pathlib
out = pathlib.Path(__file__).parent / "icons"; out.mkdir(exist_ok=True)
PAPER=(239,230,210,255); INK=(20,18,16,255)

COAT=[(3,100),(7,78),(13,64),(21,55),(30,49),(39,46),(50,45),(61,46),(70,49),(79,55),(87,64),(93,78),(97,100)]
COLLAR_L=[(40,47),(38,40),(46,45)]
COLLAR_R=[(60,47),(62,40),(54,45)]
CROWN=[(37,27),(63,27),(61,9),(57,5),(50,7),(43,5),(39,9)]

def render(size, pad=0.06):
    ss=4; S=size*ss; u=S/100.0
    big=Image.new("RGBA",(S,S),(0,0,0,0)); d=ImageDraw.Draw(big)
    P=lambda pts:[(x*u,y*u) for x,y in pts]
    d.polygon(P(COAT),fill=INK)
    d.polygon(P(COLLAR_L),fill=INK); d.polygon(P(COLLAR_R),fill=INK)
    d.ellipse([36*u,26*u,64*u,50*u],fill=INK); d.rectangle([42*u,40*u,58*u,48*u],fill=INK)  # head, neck
    d.polygon(P(CROWN),fill=INK)                          # crown with pinch
    d.ellipse([16*u,24*u,84*u,33*u],fill=INK)             # brim
    small=big.resize((size,size),Image.LANCZOS)
    canvas=Image.new("RGBA",(size,size),PAPER)
    p=int(size*pad); inner=small.resize((size-2*p,size-2*p),Image.LANCZOS)
    canvas.alpha_composite(inner,(p,p))
    return canvas.convert("RGB")

for s in (32,180,192,512): render(s).save(out/f"icon-{s}.png")
render(512,pad=0.16).save(out/"icon-maskable-512.png")
pts=lambda L:" ".join(f"{x} {y}" for x,y in L)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" fill="#efe6d2"/>
<g fill="#141210" transform="translate(6 6) scale(.88)"><polygon points="{pts(COAT)}"/><polygon points="{pts(COLLAR_L)}"/><polygon points="{pts(COLLAR_R)}"/>
<ellipse cx="50" cy="38" rx="14" ry="12"/><rect x="42" y="40" width="16" height="8"/><polygon points="{pts(CROWN)}"/><ellipse cx="50" cy="28.5" rx="34" ry="4.5"/></g></svg>'''
(out/"icon.svg").write_text(svg,encoding="utf-8")
print("ok")
