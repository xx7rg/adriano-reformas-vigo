import os

BASE = os.path.dirname(os.path.abspath(__file__))

# Same item list as build.py, kept in sync manually.
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
      <img src="selected/img_{num}.jpg" alt="{cap}" loading="lazy">
      <div class="g-cap">{cap}</div>
    </div>''')

gallery_markup = "\n    ".join(gallery_html)

with open(os.path.join(BASE, "template.html"), "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("{{GALLERY_ITEMS}}", gallery_markup)
html = html.replace("{{LOGO_MARK}}", "selected/logo_mark.png")
html = html.replace("{{LOGO_WORD}}", "selected/logo_wordmark.png")
html = html.replace("{{X7RG_LOGO}}", "selected/x7rg_mark.png")
html = html.replace("{{HERO}}", "selected/img_38.jpg")

for num, cat, cap, wide in items:
    token = "{{IMG_%s}}" % num
    html = html.replace(token, f"selected/img_{num}.jpg")

# The source template is a bare fragment (no doctype/html/head/body) meant to
# be dropped into a wrapper by whatever build step uses it. Wrap it properly
# here so the deployed page isn't served in quirks mode.
head, body = html.split("</style>", 1)
html = (
    "<!DOCTYPE html>\n<html lang=\"es\">\n<head>\n"
    "<meta charset=\"UTF-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
    + head + "</style>\n</head>\n<body>" + body + "\n</body>\n</html>\n"
)

out_path = os.path.join(BASE, "index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print("written", out_path, os.path.getsize(out_path)/1024, "KB")
