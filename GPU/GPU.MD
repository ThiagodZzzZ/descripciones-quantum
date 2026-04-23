# 📋 GUÍA: Crear Descripciones de GPU para Quantum Hardstore

## Modelo Base
**Archivo de referencia:** `msi-rtx3080ti-ventus-3x-outlet.html`

Este es el archivo plantilla que debe ser usado como modelo EXACTO para todas las nuevas descripciones de GPU.

## Proceso de Creación

### 1. Copiar la estructura base
- Usar el contenido completo de `msi-rtx3080ti-ventus-3x-outlet.html` como template
- No modificar la estructura HTML ni CSS
- No cambiar nombres de clases ni IDs

### 2. Modificaciones permitidas

#### A. Información del Producto
- **Línea 203-206:** Header (brand, manufacturer, title, subtitle)
- **Línea 209-211:** Badges (características principales + TDP)
- **Línea 216-217:** Highlight box (Boost Clock + Arquitectura)

#### B. Especificaciones Técnicas
- **Línea 220-222:** Cards (Memoria, Cores, Bus)
- **Línea 226-227:** Clock bars (Base Clock % y valores)
- **Línea 231-238:** Cooling system (nombre y características)
- **Línea 242-255:** Especificaciones table (todos los datos)
- **Línea 258-261:** Conectividad
- **Línea 264-266:** Dimensiones
- **Línea 271:** TDP y conectores en PSU
- **Línea 294:** Software incluido

#### C. GPU Database (JavaScript)
- **Línea 447:** Información base de la GPU
- **Línea 412:** Valores de PSU_MIN y GPU_TDP
- **Línea 448-460:** Comparadores alternativos (pueden mantenerse o modificarse)

### 3. Cambios Críticos por Arquitectura

#### Para NVIDIA (Ampere, Blackwell, Ada)
- Usar CUDA Cores (no Stream Processors)
- Mantener color ROSA de barras (#c0005e, #e0007a base / #ff007f, #ff4da6 boost)
- Nomenclatura: DLSS, Tensor Cores, NVIDIA Reflex

#### Para AMD (RDNA 2, RDNA 3, RDNA 4)
- Usar Stream Processors (no CUDA Cores)
- Mantener color ROSA para barras (NO cambiar a naranja)
- Nomenclatura: FreeSync, Smart Access Memory (SAM), Ray Tracing

### 4. Valores a Actualizar por GPU

| Campo | Línea | Cambiar |
|-------|-------|---------|
| Modelo/Nombre | 205 | Nombre completo GPU |
| Manufacturer | 204 | Marca (MSI, ASUS, PowerColor, etc.) |
| Memoria | 220, 448 | GB y tipo (GDDR6/GDDR6X/GDDR7) |
| Cores/SP | 221, 448 | CUDA Cores o Stream Processors |
| Boost Clock | 216, 227, 448 | MHz del GPU |
| Base Clock | 226, 403-404 | MHz base (cálculo: 73.3% del boost) |
| Bus | 222, 448 | 128/192/256/384-bit |
| Bandwidth | 222, 248, 448 | GB/s (calcular: cores × memoria speed / 8) |
| TDP | 212, 271, 412, 448 | Watts |
| PSU_MIN | 412 | Mínimo recomendado (sumar ~300W CPU) |

### 5. Cálculos Importantes

**Base Clock Bar Width:**
```
width = (BaseClockMHz / BoostClockMHz) × 100%
Ej: 1365 / 1860 = 73.3%
```

**Memory Bandwidth:**
```
BW = (Bus Width in bits × Memory Speed in Gbps) / 8
Ej: (384 × 19) / 8 = 912 GB/s
```

**PSU Minimum:**
```
PSU_MIN = GPU_TDP + ~300W (para CPU + periféricos)
Ej: 350W GPU + 300W = 650W recomendado
```

### 6. Colores: ROSA ES LA IDENTIDAD

🚨 **CRÍTICO: EL COLOR ROSA (#ff007f) ES SAGRADO — NUNCA CAMBIA**

El ROSA es la identidad visual de **Quantum Hardstore**. TODOS los productos, sin excepción, usan ROSA.

**Colores PERMITIDOS (todos con ROSA):**
- Bar base: `linear-gradient(90deg,#c0005e,#e0007a)` ← ROSA oscuro
- Bar boost: `linear-gradient(90deg,#ff007f,#ff4da6)` ← ROSA claro
- VS card right: `#ff007f` ← ROSA puro
- Performance fill: `linear-gradient(90deg,#ff007f,#ff4da6)` ← ROSA
- Border/accent: `#ff007f` ← ROSA
- Platinum glow: `rgba(255,0,127,.5)` ← ROSA

**Colores PROHIBIDOS:**
- ❌ Naranja (#ff6b00, #ff8500, #ff9900, #ffb300)
- ❌ Azul (#00d4ff, #00e6ff)
- ❌ Cualquier otro color que no sea ROSA

**REGLA DE ORO:**
Si ves un color que NO sea ROSA en gradientes, bordes o acentos → **ES UN ERROR**

### 7. Template Strings a Actualizar

**Software:**
- NVIDIA: "NVIDIA GeForce Experience • NVIDIA Broadcast • NVIDIA ShadowPlay • NVIDIA Reflex • NVIDIA DLSS"
- AMD: "AMD Radeon Software • AMD Radeon Pro • FreeSync • Smart Access Memory (SAM) • Ray Tracing"

**Cooling System (líneas 231-238):**
Cambiar según modelo específico (VENTUS X3, TUF, GAMING OC, etc.)

**Location Box - OUTLET (Retiro Inmediato):**
```html
<div class="location-box">
  <div class="location-title">📍 Producto en Local</div>
  <div class="loc-content">
    <div class="loc-icon">🏪</div>
    <div class="loc-status">RETIRO INMEDIATO</div>
    <div class="loc-desc">El producto se encuentra en nuestro local.<br>Podés retirarlo en el día al concretar tu compra.</div>
  </div>
</div>
```

**Location Box - NUEVO (En Depósito):**
```html
<div class="location-box">
  <div class="location-title">📍 Producto en Depósito</div>
  <div class="loc-content">
    <div class="loc-icon">📦</div>
    <div class="loc-status">2-3 DÍAS HÁBILES APROX.</div>
    <div class="loc-desc">El producto se encuentra en nuestro depósito.<br>Tiempo aproximado de llegada al local: 2-3 días hábiles.<br>Una vez en el local, podés coordinar retiro o envío a tu domicilio.</div>
  </div>
</div>
```

### 8. GPU Database Entry

```javascript
nombreGpu:{
  name:'Modelo Completo',
  mfr:'Manufacturer',
  model:'GPU Model',
  status:'OUTLET/NUEVA',
  vram:'12GB GDDR6X',
  cores:10240,
  boost:1860,
  bus:'384-bit',
  bw:936,
  tdp:350,
  perf:100
}
```

### 9. Publicar en GitHub con iframe

Una vez completado el archivo HTML:

**URL Base (GitHub Pages):**
```
https://ThiagodZzzZ.github.io/descripciones-quantum/[NOMBRE-ARCHIVO].html
```

**Template de iframe (copiar y pegar directamente):**
```html
<p><iframe style="border: none; display: block; width: 100%;" src="https://ThiagodZzzZ.github.io/descripciones-quantum/[NOMBRE-ARCHIVO].html" width="100%" height="4300" frameborder="0" scrolling="no"></iframe></p>
```

### 10. Validación de Datos Oficiales

**CRÍTICO:** Todos los datos DEBEN ser de fuentes oficiales:

| GPU | Fuente Oficial |
|-----|---|
| NVIDIA | nvidia.com/en-us/geforce/ |
| AMD | amd.com/en/products/graphics/ |
| MSI | msi.com/Graphics-Card |
| ASUS | asus.com/support/download-center/ |
| PowerColor | powercolor.com/products/ |
| Gigabyte | gigabyte.com/Graphics-Card/ |

**Datos a verificar SIEMPRE:**
- ✓ Memoria (GB y tipo: GDDR6/GDDR6X/GDDR7)
- ✓ CUDA Cores / Stream Processors (exactos)
- ✓ Boost Clock (MHz)
- ✓ Base Clock (MHz)
- ✓ Bus Width (bits)
- ✓ Memory Bandwidth (GB/s)
- ✓ TDP (Watts) — CRÍTICO
- ✓ Conectividad (HDMI/DisplayPort)
- ✓ Dimensiones (largo × alto × ancho)

### 11. Nomenclatura: OUTLET vs NUEVO

**OUTLET (Producto en Local):**
- Nombre del archivo: `[MARCA]-[MODELO]-**outlet.html`
- Status en JavaScript: `status:'OUTLET'`
- Ubicación: **EN EL LOCAL** (SI O SÍ)
- Disponibilidad: **RETIRO INMEDIATO**
- Descripción: Devolución de cliente / Producto reacondicionado
- Prueba: **30 DÍAS** (no 60)
- Garantía: 1 AÑO (fabricante)
- Location Box: "RETIRO INMEDIATO — El producto se encuentra en nuestro local"
- Ejemplo: `powercolor-rx6700-fighter-outlet.html`

**NUEVO (Producto Nuevo):**
- Nombre del archivo: `[MARCA]-[MODELO]-**nueva.html`
- Status en JavaScript: `status:'NUEVA'`
- Ubicación: **EN DEPÓSITO**
- Disponibilidad: Se debe coordinar retiro o envío
- Tiempo aproximado: **2-3 días hábiles** (depósito → local)
- Descripción: Producto nuevo, sin abrir
- Garantía: Completa (fabricante)
- Location Box: "EN DEPÓSITO — Tiempo aproximado 2-3 días hábiles. Se puede coordinar retiro en el local una vez llegue la mercadería"
- Ejemplo: `gigabyte-rtx5070-gaming-oc-nueva.html`

## 12. Errores Comunes — NO REPETIR

| Error | Solución | Ubicación |
|-------|----------|-----------|
| 🔴 Cambiar color a naranja/azul | ROSA SIEMPRE #ff007f | Barras, borders, gradientes |
| 🔴 Poner 60 días de prueba | OUTLET = 30 días exacto | Outlet box HTML |
| 🔴 Decir OUTLET está en depósito | OUTLET = Local retiro inmediato | Location box |
| 🔴 Olvidar TDP en badge | TDP va en badges | Línea ~211 |
| 🔴 Olvidar TDP en PSU | TDP va en PSU box subtitle | Línea ~271 |
| 🔴 Olvidar TDP en JavaScript | TDP va en const GPU_TDP | Línea ~412 |
| 🔴 Base clock % incorrecto | Calcular: (base/boost)×100 | Línea ~403-404 |
| 🔴 Nombre sin OUTLET/NUEVA | Archivo debe indicar tipo | Nombre archivo |
| 🔴 Datos de Wikipedia/YouTube | SOLO fuentes OFICIALES | Todas las specs |
| 🔴 Olvidar iframe al final | SIEMPRE proporcionar en chat | Después de terminar |

## 13. Flujo Completo: Paso a Paso

**1. RECIBIR NOMBRE DEL PRODUCTO**
- Ejemplo: "ASUS RTX 4070 TUF OC (OUTLET)"
- Identificar: (OUTLET) = local / sin parentesis = depósito

**2. COPIAR PLANTILLA**
- Usar: `msi-rtx3080ti-ventus-3x-outlet.html`
- Cambiar nombre archivo según producto exacto

**3. RECOLECTAR DATOS OFICIALES**
- Ir a sitio oficial del fabricante
- Anotar TODOS los valores técnicos
- Verificar TDP especialmente

**4. EDITAR ARCHIVO**
- Header, badges, especificaciones
- Colores: SOLO ROSA (#ff007f)
- Location box: según OUTLET o NUEVO
- Días prueba: OUTLET = 30 (no 60)

**5. VALIDAR**
- Checklist 100% completado
- Datos verificados con oficial
- Colores correctos (ROSA)
- Archivo nominado correctamente

**6. PROPORCIONAR IFRAME**
- Template: `<p><iframe style="border: none; display: block; width: 100%;" src="https://ThiagodZzzZ.github.io/descripciones-quantum/[ARCHIVO].html" width="100%" height="4300" frameborder="0" scrolling="no"></iframe></p>`
- Reemplazar [ARCHIVO] por nombre real
- Pegar EN EL CHAT para el usuario

## Checklist de Validación

### Validación Técnica
- [ ] Estructura HTML sin cambios
- [ ] CSS minificado intacto
- [ ] Todos los valores técnicos correctos
- [ ] TDP actualizado en badge, PSU box y JS
- [ ] Colores correctos según arquitectura
- [ ] Cooling system relevante al modelo
- [ ] Software apropiado al manufacturer
- [ ] Base clock % calculado correctamente
- [ ] Bandwidth calculado correctamente
- [ ] GPU database entry completo

### Validación de Datos
- [ ] Memoria verificada en sitio oficial
- [ ] CUDA Cores / Stream Processors verificados
- [ ] Boost Clock verificado
- [ ] Base Clock verificado
- [ ] Bus Width verificado
- [ ] Memory Bandwidth calculado o verificado
- [ ] TDP verificado (CRÍTICO)
- [ ] Conectividad verificada
- [ ] Dimensiones verificadas
- [ ] Arquitectura correcta

### Validación de Nombre y Status
- [ ] Archivo nombrado correctamente ([MARCA]-[MODELO]-outlet/nueva.html)
- [ ] Status correcto en JS (OUTLET o NUEVA)
- [ ] Descripción OUTLET si corresponde
- [ ] Badges actualizados con TDP

### Publicación
- [ ] Archivo guardado en `/Descripciones/GPU/`
- [ ] Commitear a GitHub
- [ ] iframe URL correcta: `https://ThiagodZzzZ.github.io/descripciones-quantum/[ARCHIVO].html`
- [ ] iframe pegado en Tiendanube con formato correcto

---

**Última actualización:** 2026-04-23
**Modelo base versión:** MSI RTX 3080 Ti Ventus X3 (OUTLET)
**Repositorio GitHub:** https://github.com/ThiagodZzzZ/descripciones-quantum
**Base de datos:** Tiendanube Quantum Hardstore
**Restricciones críticas:**
- 🎨 ROSA #ff007f es SAGRADO — NUNCA cambia
- 📅 OUTLET = 30 días prueba, EN LOCAL, RETIRO INMEDIATO
- 🆕 NUEVO = 2-3 días hábiles, EN DEPÓSITO, coordinar
- 📋 Datos SOLO de fuentes OFICIALES
- 🔗 Proporcionar iframe SIEMPRE al finalizar
