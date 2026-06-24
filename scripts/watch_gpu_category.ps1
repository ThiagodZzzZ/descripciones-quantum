param(
  [int]$IntervalMinutes = 10,
  [string]$RepoRoot = ""
)

$ErrorActionPreference = "Continue"

if (-not $RepoRoot) {
  $RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
}

$checkScript = Join-Path $RepoRoot "scripts\check_gpu_category.ps1"
$logDir = Join-Path $RepoRoot ".monitor"
$logPath = Join-Path $logDir "gpu-monitor.log"
if (-not (Test-Path -LiteralPath $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }

function Write-Log([string]$Text) {
  $line = "$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) $Text"
  Add-Content -LiteralPath $logPath -Value $line -Encoding UTF8
}

function Show-GpuNotification([string]$Message) {
  try {
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing
    $notify = New-Object System.Windows.Forms.NotifyIcon
    $notify.Icon = [System.Drawing.SystemIcons]::Information
    $notify.BalloonTipTitle = "Quantum Hardstore"
    $notify.BalloonTipText = $Message
    $notify.Visible = $true
    $notify.ShowBalloonTip(12000)
    Start-Sleep -Seconds 13
    $notify.Dispose()
  } catch {
    Write-Log "No se pudo mostrar notificacion: $($_.Exception.Message)"
  }
}

Write-Log "Monitor iniciado. Intervalo: $IntervalMinutes minutos."

while ($true) {
  try {
    $output = & powershell.exe -NoProfile -ExecutionPolicy Bypass -File $checkScript 2>&1
    $exit = $LASTEXITCODE
    foreach ($line in $output) { Write-Log $line }

    if ($exit -eq 2) {
      $summary = ($output | Where-Object { $_ -like " - *" } | Select-Object -First 2) -join "; "
      if (-not $summary) { $summary = "Hay una GPU nueva para describir." }
      Show-GpuNotification "GPU nueva detectada. Revisar .monitor\alerts. $summary"
    }
  } catch {
    Write-Log "Error monitor: $($_.Exception.Message)"
  }

  Start-Sleep -Seconds ([Math]::Max(60, $IntervalMinutes * 60))
}
