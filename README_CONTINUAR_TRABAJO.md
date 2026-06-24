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

## Seguimiento de GPUs nuevas

La categoria a controlar es:

`https://quantumhardstore.com/componentes/placas-de-video/`

Cada vez que se detecte una GPU nueva en esa categoria, compararla contra `generated_gpu_manifest.json` y `alias_cortos_manifest.json`. Si no existe descripcion publicada:

1. Avisar el titulo exacto detectado.
2. Confirmar modelo exacto y specs desde fuentes oficiales.
3. Generar la descripcion con la plantilla completa.
4. Publicar el HTML en GitHub Pages con alias corto.
5. Entregar el titulo exacto y el iframe final para Tiendanube.

Importante: Codex no puede avisar de forma proactiva si no esta corriendo en una sesion activa. Cuando se pida revisar la categoria, hacer el chequeo y avanzar con las nuevas GPUs encontradas.

### Monitor automatico local

Queda disponible un monitor local en PowerShell:

- Chequeo manual: `scripts\check_gpu_category.ps1`
- Iniciar monitor: `scripts\start_gpu_monitor.ps1 -IntervalMinutes 10`
- Detener monitor: `scripts\stop_gpu_monitor.ps1`

El monitor guarda estado en `.monitor\gpu_category_seen.json`, log en `.monitor\gpu-monitor.log` y alertas en `.monitor\alerts`. Si detecta una GPU nueva, genera un TXT con titulo exacto y URL del producto. En Windows intenta mostrar una notificacion del sistema, pero la alerta persistente es el archivo TXT.

En esta PC tambien quedo creado el lanzador de inicio:

`C:\Users\PC\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\QuantumGpuMonitor.cmd`

Eso arranca el monitor al iniciar sesion en Windows. La tarea programada de Windows no se uso porque `Register-ScheduledTask` devolvio acceso denegado sin permisos elevados.

## Diseno global posterior al Mundial

Todas las paginas GPU deben seguir conectadas globalmente a `quantum-theme.css`. No duplicar estilos visuales de campania dentro de cada HTML salvo casos puntuales inevitables. Cuando termine la campania Mundial/Argentina, el cambio de estilo debe resolverse principalmente editando `quantum-theme.css` y publicando ese archivo.

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
