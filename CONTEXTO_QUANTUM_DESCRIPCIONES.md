# Quantum Hardstore - contexto de descripciones

Fecha de trabajo: 2026-06-23.

## Objetivo

Crear descripciones HTML para productos de Quantum Hardstore, publicadas en GitHub Pages y pegadas en Tiendanube mediante iframe.

La plantilla visual correcta es la de:

`asrock-rx6900xt-phantom-gaming-outlet.html`

Reglas acordadas:

- Usar datos y specs solamente desde fuentes oficiales.
- No inventar salidas, medidas, clocks o conectores cuando no este confirmada la variante exacta.
- Mantener buen responsive en PC y celular.
- Evitar encoding roto: no usar emojis en el HTML fuente; para `AÑO`, usar `A&Ntilde;O`.
- El Top de CPUs debe cambiar segun la gama de la GPU.
- Debe haber Top AMD y Top Intel, como en la plantilla real.
- El verificador de fuente debe cambiar segun consumo y PSU recomendada de la GPU.
- La tematica actual es Mundial 2026 / Argentina / celeste y blanco.

## Cambio importante

La primera generacion masiva quedo demasiado simplificada. Se corrigio el enfoque creando:

`generate_gpu_pages_real_template.py`

Ese script usa el CSS real de la RX 6900 XT y genera las 50 descripciones con la estructura completa.

## Tema global

Las paginas generadas cargan:

`quantum-theme.css`

Ese archivo permite cambiar colores/base visual mensual sin editar cada descripcion. Para una nueva campania, cambiar variables CSS en ese archivo y volver a subirlo a GitHub.

## Archivos principales

- `quantum_gpu_products_current.json`: productos actuales scrapeados desde la categoria de placas.
- `generated_gpu_manifest.json`: titulo exacto, URL de producto, archivo HTML generado y familia detectada.
- `generated-gpus/`: HTMLs generados listos para subir.
- `generated-gpus/quantum-theme.css`: tema global.
- `generate_gpu_pages_real_template.py`: generador correcto.
- `asrock-rx6900xt-phantom-gaming-outlet.html`: plantilla visual de referencia.

## Publicacion

Repo:

`https://github.com/ThiagodZzzZ/descripciones-quantum`

GitHub Pages:

`https://thiagodzzzz.github.io/descripciones-quantum/ARCHIVO.html`

Iframe base:

```html
<iframe src="https://thiagodzzzz.github.io/descripciones-quantum/ARCHIVO.html" style="width:100%;height:6200px;border:0;" loading="lazy"></iframe>
```

Para las paginas generadas con plantilla completa, usar `height:6200px` para dejar margen en mobile.

## Productos excluidos

- `ASROCK | RX 6900XT PHANTOM GAMING (OUTLET)`: ya estaba hecho.
- `MSI GeForce RTX 3070 VENTUS 3X 8G (OUTLET)`: ya estaba hecho.
- `ACCESORIOS GENERICO ADAPTADOR VGA/DVI`: no es placa de video.
- `SOPORTE INTELAID PARA VIDEO WALL ANTIVANDALICO 45KG IT-VVWS`: no es placa de video.

## Verificaciones que deben correrse

- Barrido encoding: no debe aparecer `ð`, `â`, `Ã`, `ANIO`, `AÃO` ni `�`.
- Responsive local con Edge/Playwright en 320, 390, 632 y 1024 px.
- GitHub Pages: todos los HTML deben responder 200.

## Fuentes oficiales usadas como base

- AMD Radeon official product pages.
- NVIDIA GeForce official product pages.
- MSI official specs / PSU table cuando aplica.
- ASUS official PSU table cuando aplica.
- Gigabyte official product specs cuando aplica.
- PNY official specs cuando aplica.

