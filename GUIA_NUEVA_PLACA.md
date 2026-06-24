# Guia para crear una nueva descripcion GPU

## Datos necesarios

- Titulo exacto de Quantum.
- URL del producto en Quantum.
- Familia GPU.
- Marca y modelo exacto del ensamblador.
- Conectividad fisica: HDMI, DisplayPort, DVI, USB-C, VGA si aplica.
- Dimensiones: largo, alto/ancho frontal, espesor y slots.
- Fuente recomendada y consumo GPU.

## Fuentes

Usar fuentes oficiales:

- AMD Radeon official product pages.
- NVIDIA GeForce official product pages.
- Pagina oficial del ensamblador: ASUS, ASRock, Gigabyte, MSI, Palit, PNY, PowerColor, Sapphire, Zotac.
- Fichas oficiales AMD/Intel para CPUs recomendados.

## Reglas

- No inventar puertos.
- No inventar medidas.
- No usar "segun ensamblador" en la seccion de conectividad si el producto ya tiene modelo exacto.
- No dejar "AIB / Ficha / Stock" en dimensiones.
- Mantener titulo exacto como aparece en Quantum.
- Usar alias corto para Tiendanube.

## Checklist antes de publicar

1. El HTML muestra `Fuente modelo`.
2. La seccion `Conectividad` tiene filas reales como `1 x HDMI`, `3 x DisplayPort`, etc.
3. La seccion `Dimensiones` tiene medidas reales en mm y slots.
4. No aparece `Salidas segun ensamblador`.
5. No aparece `AIB / Ficha / Stock`.
6. El iframe usa archivo corto publicado.
7. La URL de GitHub Pages responde 200.
8. El preview de Tiendanube carga correctamente.

## Entrega final

Entregar siempre:

```html
TITULO EXACTO
<iframe src="https://thiagodzzzz.github.io/descripciones-quantum/alias-corto.html" style="width:100%;height:4600px;border:0;" loading="lazy"></iframe>
```
