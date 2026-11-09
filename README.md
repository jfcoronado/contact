# contact

Tarjeta de contacto digital para compartir por QR: https://jfcoronado.github.io/contact/

- `index.html` – página de contacto (los enlaces de correo, WhatsApp y LinkedIn están comentados; solo hay que activarlos).
- `contact.vcf` – vCard del botón «Guardar contacto».
- `qr.html` – QR a pantalla completa para mostrarlo en el teléfono.
- `qr.svg` / `qr.png` – QR para imprimir (gafete, diapositiva, tarjeta).
- `scripts/make_qr.py` – vuelve a generar el QR: `python3 scripts/make_qr.py [URL]`.

Para publicar: Settings → Pages → Source: «Deploy from a branch», rama `main`, carpeta `/ (root)`.
