# Quantum Hardstore - Descripciones GPU

## Estado actual

- Las 50 descripciones GPU trabajadas estan publicadas en GitHub Pages.
- Cada descripcion tiene conectividad real y dimensiones reales cargadas por modelo.
- Tambien existen alias cortos publicados para usar en Tiendanube sin romper URLs largas.
- La lista final para pegar en Tiendanube esta en `iframes_alias_cortos_publicados.txt`.

## Diseno global

El archivo global de diseno es:

`quantum-theme.css`

Para cambiar colores, radios, espaciados, layout de conectividad, dimensiones o tarjetas de CPU, editar ese archivo y subirlo al repo. Todas las paginas GPU cargan ese CSS, por lo que el cambio impacta globalmente.

## Nueva placa

Cuando Quantum publique una placa nueva:

1. Guardar titulo exacto y URL del producto.
2. Identificar familia de GPU.
3. Confirmar specs desde fuentes oficiales.
4. Confirmar conectividad y dimensiones del modelo exacto.
5. Generar el HTML con la plantilla completa.
6. Crear alias corto.
7. Subir HTML, actualizar manifiestos y publicar.
8. Entregar iframe final con el titulo exacto.

No usar datos genericos para conectividad o dimensiones. Si la ficha oficial no confirma el modelo exacto, no publicar medidas ni puertos inventados.

## Archivos clave

- `iframes_alias_cortos_publicados.txt`: titulos exactos + iframe final.
- `alias_cortos_manifest.json`: relacion titulo / archivo original / alias corto.
- `generated_gpu_manifest.json`: manifiesto de las 50 descripciones generadas.
- `quantum-theme.css`: control global de diseno.
- `generate_gpu_pages_real_template.py`: generador base con plantilla completa.

## Publicacion

Repo:

`https://github.com/ThiagodZzzZ/descripciones-quantum`

GitHub Pages:

`https://thiagodzzzz.github.io/descripciones-quantum/ARCHIVO.html`

Formato iframe:

```html
<iframe src="https://thiagodzzzz.github.io/descripciones-quantum/ALIAS.html" style="width:100%;height:4600px;border:0;" loading="lazy"></iframe>
```
