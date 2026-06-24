# Guia de diseno global

## Archivo unico de diseno

Editar:

`quantum-theme.css`

Ese archivo controla los ajustes globales para las descripciones GPU publicadas.

## Cambios comunes

Colores:

- `--qh-primary`
- `--qh-primary-soft`
- `--qh-primary-dark`
- `--qh-accent`
- `--qh-bg`
- `--qh-dark`
- `--qh-text`
- `--qh-border`

Layout:

- `--qh-radius`
- `--qh-container-max`
- `--qh-page-pad-x`
- `--qh-section-gap`
- `--qh-card-pad`

Bloques globales:

- `.conn-table`
- `.dim-box`
- `.cpu-columns`
- `.cpu-family`
- `.cpu-card`

## Regla de trabajo

Si el cambio es visual y debe aplicar a todas las paginas, hacerlo en `quantum-theme.css`.

Si el cambio es de datos especificos de una placa, hacerlo en el HTML de esa placa y actualizar manifiestos.

## Publicacion

Despues de editar `quantum-theme.css`, subir el archivo al repo. GitHub Pages puede tardar unos minutos en reflejar el cambio.
