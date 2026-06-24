$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$pidPath = Join-Path $repoRoot ".monitor\gpu-monitor.pid"

if (-not (Test-Path -LiteralPath $pidPath)) {
  Write-Output "No hay PID guardado para el monitor."
  exit 0
}

$monitorPid = (Get-Content -LiteralPath $pidPath -Raw).Trim()
if (-not $monitorPid) {
  Write-Output "PID vacio."
  exit 0
}

$proc = Get-Process -Id ([int]$monitorPid) -ErrorAction SilentlyContinue
if ($proc) {
  Stop-Process -Id ([int]$monitorPid) -Force
  Write-Output "Monitor detenido. PID=$monitorPid"
} else {
  Write-Output "El proceso del monitor no estaba corriendo. PID=$monitorPid"
}

Remove-Item -LiteralPath $pidPath -Force -ErrorAction SilentlyContinue
