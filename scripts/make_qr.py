"""Genera qr.svg y qr.png apuntando a la página de contacto.

Uso: pip install "qrcode[pil]" && python3 scripts/make_qr.py [URL]
"""
import sys
from pathlib import Path

import qrcode
import qrcode.image.svg

URL = sys.argv[1] if len(sys.argv) > 1 else "https://jfcoronado.github.io/contact/"
root = Path(__file__).resolve().parent.parent

def make():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=4)
    qr.add_data(URL)
    qr.make(fit=True)
    return qr

make().make_image(image_factory=qrcode.image.svg.SvgPathFillImage).save(root / "qr.svg")
try:
    q = make()
    q.box_size = 20  # ~600px+, suficiente para imprimir en un gafete
    q.make_image(fill_color="black", back_color="white").save(root / "qr.png")
except Exception as e:  # PIL opcional
    print("qr.png omitido:", e)
print("QR generado para", URL)
