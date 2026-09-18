import base64, os, mimetypes

BASE = os.path.dirname(os.path.abspath(__file__))
SEL = os.path.join(BASE, "selected")

def b64(path):
    mime = mimetypes.guess_type(path)[0] or "image/jpeg"
    with open(path, "rb") as f:
        data = f.read()
    return f"data:{mime};base64," + base64.b64encode(data).decode("ascii")

# num -> (category, caption, wide?)
# Captions were audited against the actual photos: three items that had been
# mislabeled as finished "reforma" shots but were really work-in-progress /
# demolition photos (36, 59) or a protective-covering shot (43) were fixed.
items = [
    ("02", "cocina", "Cocina reformada con muebles a medida", False),
    ("04", "cocina", "Cocina con encimera e inducción nuevas", True),
    ("06", "cocina", "Detalle de fregadero y encimera renovados", False),
    ("16", "cocina", "Cocina abierta con iluminación renovada", False),
    ("10", "bano", "Hornacina en porcelánico símil mármol", False),
    ("21", "bano", "Plato de ducha y suelo en porcelánico", False),
    ("22", "bano", "Ducha con hornacina y esquinas a inglete", True),
    ("23", "bano", "Revestimiento decorativo en tonos azules", False),
    ("24", "bano", "Baño con ventana e instalación revisada", False),
    ("45", "bano", "Alicatado decorativo en zona de ducha", False),
    ("53", "bano", "Alicatado en tono marfil, acabado uniforme", False),
    ("28", "reforma", "Techo y paredes recién pintados", False),
    ("38", "reforma", "Pasillo con pintura renovada", False),
    ("43", "reforma", "Protegiendo los muebles antes de pintar", False),
    ("44", "reforma", "Iluminación empotrada tras la reforma", False),
    ("46", "reforma", "Estancia pintada en tonos neutros", False),
    ("58", "reforma", "Dormitorio con molduras de techo renovadas", False),
    ("18", "exterior", "Fachada y cierre exterior de una vivienda", True),
    ("20", "exterior", "Trabajos de cierre y exterior de parcela", False),
    ("42", "exterior", "Pavimento exterior renovado", False),
    ("30", "antes", "Antes: vivienda al comenzar la reforma", False),
    ("36", "antes", "Antes: filtración de agua en el techo", True),
    ("59", "cocina", "Nicho de cocina con nevera integrada", False),
    ("60", "antes", "Antes: escombros tras la demolición", False),
]

gallery_html = []
for num, cat, cap, wide in items:
    cls = "g-item wide" if wide else "g-item"
    badge = "Antes" if cat == "antes" else {"cocina":"Cocina","bano":"Baño","reforma":"Reforma","exterior":"Exterior"}[cat]
    gallery_html.append(f'''<div class="{cls}" data-cat="{cat}">
      <span class="g-badge">{badge}</span>
      <img src="{{{{IMG_{num}}}}}" alt="{cap}">
      <div class="g-cap">{cap}</div>
    </div>''')

gallery_markup = "\n    ".join(gallery_html)

with open(os.path.join(BASE, "template.html"), "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("{{GALLERY_ITEMS}}", gallery_markup)
html = html.replace("{{LOGO_MARK}}", b64(os.path.join(SEL, "logo_mark.png")))
html = html.replace("{{LOGO_WORD}}", b64(os.path.join(SEL, "logo_wordmark.png")))
html = html.replace("{{X7RG_LOGO}}", b64(os.path.join(SEL, "x7rg_mark.png")))
html = html.replace("{{HERO}}", b64(os.path.join(SEL, "img_38.jpg")))
html = html.replace("{{FAVICON}}", b64(os.path.join(SEL, "favicon.png")))

for num, cat, cap, wide in items:
    token = "{{IMG_%s}}" % num
    html = html.replace(token, b64(os.path.join(SEL, f"img_{num}.jpg")))

out_path = os.path.join(BASE, "dist", "adriano-vigo-reformas.html")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print("written", out_path, os.path.getsize(out_path)/1024/1024, "MB")
