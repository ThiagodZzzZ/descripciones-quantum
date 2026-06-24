param(
  [int]$IntervalMinutes = 10
)

$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$watchScript = Join-Path $repoRoot "scripts\watch_gpu_category.ps1"
$logDir = Join-Path $repoRoot ".monitor"
if (-not (Test-Path -LiteralPath $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }

$args = @(
  "-NoProfile",
  "-ExecutionPolicy", "Bypass",
  "-File", "`"$watchScript`"",
  "-IntervalMinutes", "$IntervalMinutes",
  "-RepoRoot", "`"$repoRoot`""
) -join " "

$proc = Start-Process -FilePath "powershell.exe" -ArgumentList $args -WindowStyle Hidden -PassThru
"$($proc.Id)" | Set-Content -LiteralPath (Join-Path $logDir "gpu-monitor.pid") -Encoding ASCII
Write-Output "Monitor iniciado en segundo plano. PID=$($proc.Id)"
Write-Output "Log: $logDir\gpu-monitor.log"
Write-Output "Alertas: $logDir\alerts"
