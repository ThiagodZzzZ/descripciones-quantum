import json
import re
from pathlib import Path

BASE = Path(r"C:\Users\totog\descripciones-quantum")
PRODUCTS_FILE = BASE / "quantum_gpu_products_current.json"
TEMPLATE_FILE = BASE / "asrock-rx6900xt-phantom-gaming-outlet.html"
OUT = BASE / "generated-gpus"
OUT.mkdir(exist_ok=True)

PRODUCTS = json.loads(PRODUCTS_FILE.read_text(encoding="utf-8-sig"))
TEMPLATE_HTML = TEMPLATE_FILE.read_text(encoding="utf-8")
CSS = re.search(r"<style>(.*?)</style>", TEMPLATE_HTML, re.S).group(1)

EXCLUDE_PATTERNS = [
    r"ADAPTADOR VGA/DVI",
    r"SOPORTE INTELAID",
    r"ASROCK \| RX 6900XT PHANTOM",
    r"MSI GeForce RTX 3070 VENTUS 3X",
]

THEME_CSS = """/* Quantum Hardstore global theme.
   Para cambiar la campania mensual, editar solo este archivo y volver a subirlo. */
:root{
  --qh-primary:#16a8e8;
  --qh-primary-soft:#eaf8ff;
  --qh-primary-dark:#0875aa;
  --qh-accent:#f6c343;
  --qh-bg:#e9f8ff;
  --qh-panel:rgba(255,255,255,.95);
  --qh-dark:#061b2b;
  --qh-dark-2:#0b2b43;
  --qh-text:#062033;
  --qh-muted:#5c7485;
  --qh-border:#bfe8fb;
  --qh-shadow:rgba(22,168,232,.28);
}
body{background:linear-gradient(180deg,#9fe4ff 0,#fff 34%,#dff6ff 68%,#fff 100%)}
.header:after{content:"ARGENTINA 2026"}
.world-cup-ribbon{background:linear-gradient(90deg,#75cdf4,#fff,#75cdf4);color:#06486b}
"""

FAMILIES = {
    "RTX 5080": dict(brand="NVIDIA GeForce", arch="Blackwell", cores="10752 CUDA", memory="16GB GDDR7", bus="256-bit", speed="GDDR7", power=360, psu=850, pcie="PCIe 5.0", connector="Segun ensamblador", source="NVIDIA GeForce RTX 5080 oficial"),
    "RTX 5070 Ti": dict(brand="NVIDIA GeForce", arch="Blackwell", cores="8960 CUDA", memory="16GB GDDR7", bus="256-bit", speed="GDDR7", power=300, psu=750, pcie="PCIe 5.0", connector="Segun ensamblador", source="NVIDIA GeForce RTX 5070 Family oficial"),
    "RTX 5070": dict(brand="NVIDIA GeForce", arch="Blackwell", cores="6144 CUDA", memory="12GB GDDR7", bus="192-bit", speed="28 Gbps", power=250, psu=650, pcie="PCIe 5.0", connector="Segun ensamblador", source="NVIDIA GeForce RTX 5070 oficial"),
    "RTX 5060 Ti": dict(brand="NVIDIA GeForce", arch="Blackwell", cores="4608 CUDA", memory="8GB GDDR7", bus="128-bit", speed="GDDR7", power=180, psu=600, pcie="PCIe 5.0", connector="Segun ensamblador", source="NVIDIA RTX 5060 Family / PNY RTX 5060 Ti oficial"),
    "RTX 5050": dict(brand="NVIDIA GeForce", arch="Blackwell", cores="2560 CUDA", memory="8GB GDDR6", bus="128-bit", speed="GDDR6", power=130, psu=550, pcie="PCIe 5.0", connector="Segun ensamblador", source="NVIDIA GeForce RTX 5050 / MSI PSU table oficial"),
    "RTX 3050": dict(brand="NVIDIA GeForce", arch="Ampere", cores="2304 CUDA", memory="6GB GDDR6", bus="96-bit", speed="14 Gbps", power=70, psu=300, pcie="PCIe 4.0", connector="Sin conector en modelos 70W", source="NVIDIA GeForce RTX 3050 6GB oficial"),
    "RTX 3070 Ti": dict(brand="NVIDIA GeForce", arch="Ampere", cores="6144 CUDA", memory="8GB GDDR6X", bus="256-bit", speed="GDDR6X", power=290, psu=750, pcie="PCIe 4.0", connector="Segun ensamblador", source="NVIDIA GeForce RTX 3070 Family oficial"),
    "RTX 3070": dict(brand="NVIDIA GeForce", arch="Ampere", cores="5888 CUDA", memory="8GB GDDR6", bus="256-bit", speed="14 Gbps", power=220, psu=650, pcie="PCIe 4.0", connector="Segun ensamblador", source="NVIDIA GeForce RTX 3070 Family oficial"),
    "RTX 2060 SUPER": dict(brand="NVIDIA GeForce", arch="Turing", cores="2176 CUDA", memory="8GB GDDR6", bus="256-bit", speed="14 Gbps", power=175, psu=550, pcie="PCIe 3.0", connector="8-pin + 6-pin", source="Gigabyte RTX 2060 SUPER GAMING OC oficial"),
    "GT 1030": dict(brand="NVIDIA GeForce", arch="Pascal", cores="384 CUDA", memory="2GB GDDR5", bus="64-bit", speed="6008 MHz", power=30, psu=300, pcie="PCIe 3.0", connector="Sin conector", source="NVIDIA GT 1030 / ASUS PH-GT1030-O2G oficial"),
    "RX 9070 XT": dict(brand="AMD Radeon", arch="RDNA 4", cores="4096 Stream", memory="16GB GDDR6", bus="256-bit", speed="20 Gbps", power=304, psu=750, pcie="PCIe 5.0", connector="Segun ensamblador", source="AMD Radeon RX 9070 XT oficial"),
    "RX 9070": dict(brand="AMD Radeon", arch="RDNA 4", cores="3584 Stream", memory="16GB GDDR6", bus="256-bit", speed="20 Gbps", power=220, psu=650, pcie="PCIe 5.0", connector="Segun ensamblador", source="AMD Radeon RX 9070 oficial"),
    "RX 9060 XT": dict(brand="AMD Radeon", arch="RDNA 4", cores="2048 Stream", memory="16GB GDDR6", bus="128-bit", speed="20 Gbps", power=160, psu=550, pcie="PCIe 5.0", connector="1 x 8-pin usual", source="AMD Radeon RX 9060 XT / ASUS PSU table oficial"),
    "RX 7600": dict(brand="AMD Radeon", arch="RDNA 3", cores="2048 Stream", memory="8GB GDDR6", bus="128-bit", speed="18 Gbps", power=165, psu=550, pcie="PCIe 4.0", connector="1 x 8-pin usual", source="AMD Radeon RX 7600 oficial"),
    "RX 6900 XT": dict(brand="AMD Radeon", arch="RDNA 2", cores="5120 Stream", memory="16GB GDDR6", bus="256-bit", speed="16 Gbps", power=300, psu=850, pcie="PCIe 4.0", connector="Segun ensamblador", source="AMD Radeon RX 6900 XT oficial"),
    "RX 6800 XT": dict(brand="AMD Radeon", arch="RDNA 2", cores="4608 Stream", memory="16GB GDDR6", bus="256-bit", speed="16 Gbps", power=300, psu=750, pcie="PCIe 4.0", connector="Segun ensamblador", source="AMD Radeon RX 6800 XT / MSI modelo oficial"),
    "RX 6700 XT": dict(brand="AMD Radeon", arch="RDNA 2", cores="2560 Stream", memory="12GB GDDR6", bus="192-bit", speed="16 Gbps", power=230, psu=650, pcie="PCIe 4.0", connector="Segun ensamblador", source="AMD Radeon RX 6700 XT oficial"),
    "RX 570": dict(brand="AMD Radeon", arch="Polaris", cores="2048 Stream", memory="8GB GDDR5", bus="256-bit", speed="7 Gbps", power=150, psu=450, pcie="PCIe 3.0", connector="8-pin", source="Gigabyte Radeon RX 570 GAMING oficial"),
}

CPU_BANKS = {
    "high": {
        "amd": [
            ("1 - Ideal actual", "Ryzen 7 9800X3D", "8C/16T", "5.2 GHz", "96 MB", "AM5 + 3D V-Cache para FPS altos y frametime muy estable."),
            ("2 - AM5 probado", "Ryzen 7 7800X3D", "8C/16T", "5.0 GHz", "96 MB", "Gaming premium para 1440p alto refresh y 4K."),
            ("3 - AM4 fuerte", "Ryzen 7 5800X3D", "8C/16T", "4.5 GHz", "96 MB", "Upgrade ideal si ya tenes AM4 y queres empujar fuerte."),
        ],
        "intel": [
            ("1 - Plataforma nueva", "Core Ultra 7 265K", "20C/20T", "5.5 GHz", "30 MB", "Opcion Intel moderna con margen para gaming y multitarea."),
            ("2 - Muy solido", "Core i7-14700K", "20C/28T", "5.6 GHz", "33 MB", "Excelente para jugar y trabajar sin limitar la GPU."),
            ("3 - Precio/rend.", "Core i5-14600K", "14C/20T", "5.3 GHz", "24 MB", "Gran dupla para resoluciones altas."),
        ],
    },
    "mid": {
        "amd": [
            ("1 - Ideal gaming", "Ryzen 7 7800X3D", "8C/16T", "5.0 GHz", "96 MB", "Excelente margen para placas de gama media/alta."),
            ("2 - AM5 equilibrio", "Ryzen 5 7600X", "6C/12T", "5.3 GHz", "32 MB", "Muy buena frecuencia por nucleo para gaming actual."),
            ("3 - AM4 recomendado", "Ryzen 7 5700X3D", "8C/16T", "4.1 GHz", "96 MB", "Upgrade AM4 con 3D V-Cache para jugar fuerte."),
        ],
        "intel": [
            ("1 - Ideal Intel", "Core i5-14600K", "14C/20T", "5.3 GHz", "24 MB", "Rinde muy bien en gaming y multitarea."),
            ("2 - Solido", "Core i5-13600K", "14C/20T", "5.1 GHz", "24 MB", "Gran companero para 1440p."),
            ("3 - Entrada fuerte", "Core i5-12600K", "10C/16T", "4.9 GHz", "20 MB", "Suficiente para sacar buen rendimiento."),
        ],
    },
    "entry": {
        "amd": [
            ("1 - Equilibrado", "Ryzen 5 7600", "6C/12T", "5.1 GHz", "32 MB", "AM5 eficiente para placas de entrada/media."),
            ("2 - AM4 rendidor", "Ryzen 5 5600", "6C/12T", "4.4 GHz", "32 MB", "Muy buena base para 1080p."),
            ("3 - Economico", "Ryzen 5 5500", "6C/12T", "4.2 GHz", "16 MB", "Opcion accesible para equipos ajustados."),
        ],
        "intel": [
            ("1 - Actual", "Core i5-14400F", "10C/16T", "4.7 GHz", "20 MB", "Buen equilibrio para placas eficientes."),
            ("2 - Probado", "Core i5-12400F", "6C/12T", "4.4 GHz", "18 MB", "Clasico precio/rendimiento para 1080p."),
            ("3 - Basico", "Core i3-12100F", "4C/8T", "4.3 GHz", "12 MB", "Valido para GPUs de bajo consumo."),
        ],
    },
}


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


def slugify(s: str) -> str:
    s = s.lower()
    s = s.replace("|", " ").replace("+", " plus")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return "gpu-" + s[:100] + ".html"


def detect_family(title: str):
    t = title.upper().replace("GEFORCE", "").replace("RADEON", "")
    rules = [
        ("RTX 5080", r"RTX\s*5080"),
        ("RTX 5070 Ti", r"RTX\s*5070\s*TI|5070TI"),
        ("RTX 5070", r"RTX\s*5070"),
        ("RTX 5060 Ti", r"RTX\s*5060\s*TI|5060TI"),
        ("RTX 5050", r"RTX\s*5050"),
        ("RTX 3050", r"RTX\s*3050"),
        ("RTX 3070 Ti", r"RTX\s*3070\s*TI"),
        ("RTX 3070", r"RTX\s*3070"),
        ("RTX 2060 SUPER", r"2060\s*SUPER|RTX\s*2060\s*SUPER"),
        ("GT 1030", r"GT\s*1030"),
        ("RX 9070 XT", r"RX\s*9070\s*XT|RX9070XT"),
        ("RX 9070", r"RX\s*9070|RX9070"),
        ("RX 9060 XT", r"RX\s*9060\s*XT|RX9060XT"),
        ("RX 7600", r"RX\s*7600|RX7600"),
        ("RX 6900 XT", r"RX\s*6900\s*XT|RX6900XT"),
        ("RX 6800 XT", r"RX\s*6800\s*XT|RX6800XT"),
        ("RX 6700 XT", r"RX\s*6700\s*XT|RX6700XT"),
        ("RX 570", r"RX\s*570"),
    ]
    for fam, pat in rules:
        if re.search(pat, t):
            spec = FAMILIES[fam].copy()
            tu = title.upper()
            if fam == "RX 9060 XT" and ("8GB" in tu or "8G " in tu):
                spec["memory"] = "8GB GDDR6"
                spec["power"] = 150
            if fam == "RTX 5060 Ti" and "16GB" in tu:
                spec["memory"] = "16GB GDDR7"
            return fam, spec
    raise ValueError(f"No family for {title}")


def condition(title: str):
    tu = title.upper()
    if "OUTLET" in tu:
        return "OUTLET", "Producto usado, revisado y verificado por nuestro equipo tecnico. Puede presentar detalles esteticos propios del uso, sin afectar su funcionamiento."
    if "NUEVA" in tu or "NUEVO" in tu:
        return "NUEVA", "Producto nuevo publicado por Quantum Hardstore."
    return "PUBLICADA", "Producto publicado por Quantum Hardstore."


def cpu_tier(spec):
    if spec["psu"] >= 650 or spec["family"] in ("RTX 5080", "RTX 5070", "RX 9070 XT", "RX 9070", "RX 6900 XT", "RX 6800 XT"):
        return "high"
    if spec["psu"] >= 550:
        return "mid"
    return "entry"


def cpu_cards(cards):
    out = []
    for i, (rank, name, cores, boost, cache, fit) in enumerate(cards):
        gold = " gold" if i == 0 else ""
        out.append(f"""      <div class="cpu-card{gold}">
        <div class="cpu-rank">{esc(rank)}</div>
        <div class="cpu-name">{esc(name)}</div>
        <div class="cpu-specs">
          <div class="cpu-spec"><span>Nucleos</span><strong>{esc(cores)}</strong></div>
          <div class="cpu-spec"><span>Boost</span><strong>{esc(boost)}</strong></div>
          <div class="cpu-spec"><span>Cache</span><strong>{esc(cache)}</strong></div>
        </div>
        <div class="cpu-fit"><strong>Recomendado:</strong> {esc(fit)}</div>
      </div>""")
    return "\n".join(out)


def html_for(product, fam, spec):
    title = esc(product["title"])
    cond, cond_desc = condition(product["title"])
    spec["family"] = fam
    tier = cpu_tier(spec)
    cpus = CPU_BANKS[tier]
    psu_low = max(250, spec["psu"] - 200)
    psu_max = max(900, spec["psu"] + 400)
    resolution = "1440p alto refresh y 4K" if spec["psu"] >= 650 else "1080p competitivo y 1440p ajustado"
    outlet_title = "Producto OUTLET" if cond == "OUTLET" else "Garantia Quantum"
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - Quantum Hardstore</title>
<style>{CSS}</style>
<link rel="stylesheet" href="quantum-theme.css">
</head>
<body>
<button class="back-top" id="back-top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})" title="Volver arriba">^</button>
<div class="container">

<div class="header">
  <div class="header-brand">Quantum Hardstore</div>
  <div class="header-manufacturer">{esc(spec['brand'])}</div>
  <div class="header-title">{title}</div>
  <div class="header-subtitle">{cond} / {esc(spec['memory'])} / {esc(spec['pcie'])} / {esc(spec['arch'])} / {spec['power']}W GPU</div>
  <div class="world-cup-ribbon">Promos Mundial 2026 - Celeste y blanco</div>
</div>

<div class="badges">
  <span class="badge">{esc(spec['arch'])}</span>
  <span class="badge">{esc(spec['memory'])}</span>
  <span class="badge">{esc(spec['bus'])}</span>
  <span class="badge">{esc(spec['pcie'])}</span>
  <span class="badge">{spec['psu']}W PSU</span>
  <span class="badge">{cond}</span>
</div>

<div class="match-strip">
  <div class="match-copy">
    <div class="match-kicker">Mundial - Placas de video</div>
    <div class="match-title">{esc(fam)} para jugar con margen en <span>{resolution}.</span></div>
    <div class="match-note">Specs base verificadas con fuentes oficiales. En variantes AIB, salidas, clocks y dimensiones pueden cambiar segun ensamblador.</div>
    <div class="match-meter">
      <div class="meter-card"><div class="meter-label">Arquitectura</div><div class="meter-value">{esc(spec['arch'])}</div><div class="meter-note">{esc(spec['brand'])}</div></div>
      <div class="meter-card"><div class="meter-label">Memoria</div><div class="meter-value">{esc(spec['memory'].split()[0])}</div><div class="meter-note">{esc(spec['speed'])} - {esc(spec['bus'])}</div></div>
      <div class="meter-card"><div class="meter-label">Fuente</div><div class="meter-value">{spec['psu']}W</div><div class="meter-note">Recomendada base</div></div>
    </div>
  </div>
  <div class="match-score">
    <div class="score-chip">{esc(fam).replace(' ', '<br>')}</div>
    <div class="score-chip">{cond}<br>OK</div>
  </div>
</div>

<div class="play-grid">
  <div class="play-card">
    <div class="play-kicker">Jugada clave</div>
    <div class="play-title">Rendimiento bien ubicado: {esc(spec['cores'])}, {esc(spec['memory'])} y fuente recomendada de {spec['psu']}W.</div>
    <div class="play-copy">Una placa pensada para equipos gamer segun su gama. La informacion tecnica evita mezclar modelos: se toman datos oficiales del GPU/familia y se aclara cuando la variante exacta depende del ensamblador.</div>
    <div class="play-pills">
      <span class="play-pill">{esc(fam)}</span>
      <span class="play-pill">{esc(spec['pcie'])}</span>
      <span class="play-pill">{esc(spec['connector'])}</span>
      <span class="play-pill">{spec['psu']}W PSU</span>
    </div>
  </div>
  <div class="benefit-panel">
    <div class="benefit-list">
      <div class="benefit-item"><div class="benefit-ico">1</div><div class="benefit-txt"><b>Gaming fluido</b><span>Rendimiento acorde a {esc(fam)}.</span></div></div>
      <div class="benefit-item"><div class="benefit-ico">2</div><div class="benefit-txt"><b>Imagen nitida</b><span>Lista para monitores modernos.</span></div></div>
      <div class="benefit-item"><div class="benefit-ico">3</div><div class="benefit-txt"><b>Fuente clara</b><span>Verificador con margen real.</span></div></div>
      <div class="benefit-item"><div class="benefit-ico">OK</div><div class="benefit-txt"><b>Datos oficiales</b><span>Sin specs inventadas.</span></div></div>
    </div>
  </div>
</div>

<div class="engine">
  <div class="engine-title">Velocidad y memoria</div>
  <div class="clock-item"><div class="clock-label">Procesamiento GPU</div><div class="bar-bg"><div class="bar bar-boost" id="core-bar" style="width:0%">{esc(spec['cores'])}</div></div></div>
  <div class="clock-item"><div class="clock-label">Consumo GPU oficial/base</div><div class="bar-bg"><div class="bar bar-boost" id="game-bar" style="width:0%">{spec['power']}W</div></div></div>
  <div class="clock-item"><div class="clock-label">Memoria</div><div class="bar-bg"><div class="bar bar-base" id="mem-bar" style="width:0%">{esc(spec['memory'])}</div></div></div>
</div>

<div class="cooling">
  <div class="cooling-title">Disenio del ensamblador</div>
  <div class="cooling-sub">Cada modelo usa su propio disipador, cantidad de ventiladores, backplate y clocks. No se inventan medidas ni salidas cuando no estan confirmadas en ficha oficial.</div>
  <div class="cooling-features">
    <div class="cf"><div class="cf-name">GPU {esc(fam)}</div><div class="cf-label">Base tecnica oficial de la familia del chip grafico.</div></div>
    <div class="cf"><div class="cf-name">{esc(spec['memory'])}</div><div class="cf-label">Memoria declarada segun producto/familia.</div></div>
    <div class="cf"><div class="cf-name">{esc(spec['arch'])}</div><div class="cf-label">Arquitectura oficial de la generacion.</div></div>
    <div class="cf"><div class="cf-name">{spec['psu']}W PSU</div><div class="cf-label">Margen recomendado para una PC gamer completa.</div></div>
  </div>
</div>

<div class="section-title"><span>Especificaciones oficiales</span></div>
<div class="spec-board">
  <div class="spec-hero">
    <span class="spec-tag">Ficha verificada</span>
    <div class="spec-gpu">{esc(fam)}</div>
    <div class="spec-model">{title} - {esc(spec['arch'])} - {esc(spec['pcie'])}</div>
    <div class="spec-mini">
      <div><span>GPU</span><strong>{esc(spec['cores'])}</strong></div>
      <div><span>Memoria</span><strong>{esc(spec['memory'])}</strong></div>
      <div><span>Bus</span><strong>{esc(spec['bus'])}</strong></div>
      <div><span>Consumo</span><strong>{spec['power']}W</strong></div>
    </div>
  </div>
  <div class="spec-list">
    <div class="spec-item"><span>Memoria</span><strong>{esc(spec['speed'])} - {esc(spec['bus'])}</strong></div>
    <div class="spec-item"><span>Energia</span><strong>{esc(spec['connector'])} - PSU {spec['psu']}W</strong></div>
    <div class="spec-item"><span>PCI Express</span><strong>{esc(spec['pcie'])}</strong></div>
    <div class="spec-item"><span>Arquitectura</span><strong>{esc(spec['arch'])}</strong></div>
    <div class="spec-item"><span>Fuente specs</span><strong>{esc(spec['source'])}</strong></div>
    <div class="spec-item"><span>Nota AIB</span><strong>Clocks, salidas y medidas pueden variar por modelo exacto</strong></div>
  </div>
</div>

<div class="section-title"><span>Conectividad</span></div>
<div class="conn-table">
  <div><span class="conn-chip">AIB</span><div class="conn-info"><b>Salidas segun ensamblador</b><small>HDMI/DisplayPort pueden variar entre ASUS, Gigabyte, PowerColor, Sapphire, MSI, Zotac, Palit o PNY.</small></div><span class="conn-count">OK</span></div>
  <div><span class="conn-chip">GPU</span><div class="conn-info"><b>Soporte digital de la familia {esc(fam)}</b><small>Usar siempre la ficha oficial del modelo exacto para validar puertos fisicos.</small></div><span class="conn-count">REF</span></div>
</div>

<div class="section-title"><span>Dimensiones</span></div>
<div class="dim-box">
  <div class="d"><b>AIB</b><small>Modelo exacto</small></div><span class="sep">/</span>
  <div class="d"><b>Ficha</b><small>Fabricante</small></div><span class="sep">/</span>
  <div class="d"><b>Stock</b><small>Validar gabinete</small></div>
</div>

<div class="psu-box">
  <div class="psu-title">Verificador de fuente</div>
  <div class="psu-sub">Consumo GPU: {spec['power']}W / Conectores: {esc(spec['connector'])} / Fuente recomendada base: {spec['psu']}W</div>
  <div class="psu-row">
    <span class="psu-lbl">Watts de tu fuente</span>
    <input type="range" class="psu-range" min="{psu_low}" max="{psu_max}" step="50" value="{spec['psu']}" id="psu-slider">
    <span class="psu-out" id="psu-out">{spec['psu']} W</span>
  </div>
  <div class="psu-grid">
    <div class="pcb a-sin" id="cert-sin" onclick="setCert('sin')">Sin cert.</div>
    <div class="pcb" id="cert-bronze" onclick="setCert('bronze')">Bronze</div>
    <div class="pcb" id="cert-silver" onclick="setCert('silver')">Silver</div>
    <div class="pcb" id="cert-gold" onclick="setCert('gold')">Gold</div>
    <div class="pcb" id="cert-plat" onclick="setCert('plat')">Platinum</div>
  </div>
  <div class="psu-result" id="psu-result">
    <div class="psu-icon" id="psu-icon">?</div>
    <div class="psu-status" id="psu-status">Selecciona tu fuente</div>
    <div class="psu-desc" id="psu-desc">Move el slider y elegi certificacion para ver el diagnostico.</div>
  </div>
</div>

<div class="cpu-box">
  <div class="cpu-head">
    <div class="cpu-kicker">Top CPUs recomendados</div>
    <div class="cpu-title">Procesadores para acompa&ntilde;ar {esc(fam)} con buen margen</div>
    <div class="cpu-sub">Selecciones pensadas para gaming fluido con esta GPU. Specs de CPU tomadas de AMD e Intel oficiales; el resultado final depende de resolucion, RAM, juego y configuracion.</div>
  </div>
  <div class="cpu-columns">
    <div class="cpu-family">
      <div class="family-title"><b>AMD Ryzen</b><span class="family-pill">Celeste</span></div>
{cpu_cards(cpus['amd'])}
    </div>
    <div class="cpu-family">
      <div class="family-title"><b>Intel Core</b><span class="family-pill">Blanco</span></div>
{cpu_cards(cpus['intel'])}
    </div>
  </div>
  <div class="bottle-note"><strong>Nota honesta:</strong> "0 cuello de botella" absoluto no existe en PC porque cambia segun juego, resolucion, graficos, RAM y procesos abiertos. Estos CPUs estan elegidos para que el cuello de botella sea practicamente nulo en un armado bien configurado para la gama de esta GPU.</div>
</div>

<div class="outlet-box">
  <div class="outlet-title">{esc(outlet_title)}</div>
  <div class="outlet-desc">{esc(cond_desc)}</div>
  <div class="outlet-benefits">
    <div class="ob"><div class="ob-val">30 DIAS</div><div class="ob-lbl">DE PRUEBA</div></div>
    <div class="ob"><div class="ob-val">1 A&Ntilde;O</div><div class="ob-lbl">DE GARANTIA</div></div>
  </div>
</div>

<div class="note">Specs verificadas con fuentes oficiales: {esc(spec['source'])}, paginas oficiales AMD/NVIDIA y fichas oficiales de CPU AMD/Intel para procesadores recomendados.</div>

</div>
<script>
window.addEventListener('load',()=>setTimeout(()=>{{
  document.getElementById('core-bar').style.width='100%';
  document.getElementById('game-bar').style.width='90%';
  document.getElementById('mem-bar').style.width='86%';
}},400));

const PSU_MIN={spec['psu']},GPU_TDP={spec['power']};
let cert='sin',watts={spec['psu']};
const cNames={{sin:'sin certificacion',bronze:'80 Plus Bronze',silver:'80 Plus Silver',gold:'80 Plus Gold',plat:'80 Plus Platinum'}};
const cWarn={{
  sin:'<strong>Sin 80 Plus:</strong> conviene dejar mas margen porque la eficiencia y estabilidad pueden ser menores.',
  bronze:'<strong>80 Plus Bronze:</strong> funciona como base, pero Gold o superior es mejor para gaming sostenido.',
  silver:'<strong>80 Plus Silver:</strong> correcto, aunque Gold suma margen termico y electrico.',
  gold:'',
  plat:''
}};
function setCert(c){{
  cert=c;
  ['sin','bronze','silver','gold','plat'].forEach(x=>{{
    document.getElementById('cert-'+x).className='pcb'+(x===c?' a-'+c:'');
  }});
  evalPSU();
}}
function evalPSU(){{
  const w=watts,box=document.getElementById('psu-result'),
    ico=document.getElementById('psu-icon'),sta=document.getElementById('psu-status'),dsc=document.getElementById('psu-desc');
  box.className='psu-result';
  const certText=cert!=='sin'?' con '+cNames[cert]:' '+cNames[cert];
  const warn=cWarn[cert]?'<br><br>'+cWarn[cert]:'';
  if(w<Math.max({psu_low},PSU_MIN-150)){{
    box.classList.add('psu-danger');ico.textContent='!';
    sta.textContent='No recomendado';
    dsc.innerHTML=w+'W es insuficiente para una GPU de '+GPU_TDP+'W y una PC gamer completa. Conviene apuntar a '+PSU_MIN+'W o mas.'+warn;
  }}else if(w<PSU_MIN){{
    box.classList.add('psu-warn');ico.textContent='!';
    sta.textContent='Funciona al limite';
    dsc.innerHTML='Con '+w+'W estas por debajo de la recomendacion base de '+PSU_MIN+'W. Conviene mejorar la fuente antes de exigir la PC.'+warn;
  }}else if(w<=PSU_MIN+150){{
    box.classList.add('psu-ok');ico.textContent='OK';
    sta.textContent='Fuente suficiente';
    dsc.innerHTML=w+'W'+certText+' cumple el margen base para esta placa.'+warn;
  }}else{{
    box.classList.add('psu-great');ico.textContent='OK';
    sta.textContent='Margen amplio';
    dsc.innerHTML=w+'W'+certText+' ofrece margen para CPU potente, perifericos y futuros upgrades moderados.'+warn;
  }}
}}
document.getElementById('psu-slider').addEventListener('input',function(){{
  watts=parseInt(this.value,10);
  document.getElementById('psu-out').textContent=watts+' W';
  evalPSU();
}});
evalPSU();

const btn=document.getElementById('back-top');
window.addEventListener('scroll',()=>{{btn.style.display=window.scrollY>300?'flex':'none';}});

function adjustIframeHeight(){{
  try{{window.parent.postMessage({{type:'resize',height:document.body.scrollHeight}},'*')}}catch(e){{}}
}}
window.addEventListener('load',adjustIframeHeight);
window.addEventListener('resize',adjustIframeHeight);
document.addEventListener('click',adjustIframeHeight);
document.addEventListener('change',adjustIframeHeight);
new MutationObserver(adjustIframeHeight).observe(document.body,{{childList:true,subtree:true,attributes:true,attributeFilter:['style','class']}});
</script>
</body>
</html>
"""


manifest = []
seen = {}
(OUT / "quantum-theme.css").write_text(THEME_CSS, encoding="utf-8")
for p in PRODUCTS:
    if any(re.search(x, p["title"], re.I) for x in EXCLUDE_PATTERNS):
        continue
    fam, spec = detect_family(p["title"])
    fn = slugify(p["title"])
    if fn in seen:
        seen[fn] += 1
        fn = fn.replace(".html", f"-{seen[fn]}.html")
    else:
        seen[fn] = 1
    (OUT / fn).write_text(html_for(p, fam, spec), encoding="utf-8")
    manifest.append({"title": p["title"], "product_url": p["url"], "file": fn, "family": fam})

(BASE / "generated_gpu_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=True), encoding="utf-8")
print(f"generated={len(manifest)}")
for row in manifest:
    print(f"{row['file']} | {row['title']}")
