param(
  [string]$CategoryUrl = "https://quantumhardstore.com/componentes/placas-de-video/",
  [string]$RepoRoot = "",
  [string]$StatePath = "",
  [string]$AlertDir = "",
  [switch]$Initialize
)

$ErrorActionPreference = "Stop"

if (-not $RepoRoot) {
  $RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
}
if (-not $StatePath) {
  $StatePath = Join-Path $RepoRoot ".monitor\gpu_category_seen.json"
}
if (-not $AlertDir) {
  $AlertDir = Join-Path $RepoRoot ".monitor\alerts"
}

function Normalize-Text([string]$Value) {
  if ($null -eq $Value) { return "" }
  $decoded = [System.Net.WebUtility]::HtmlDecode($Value)
  return (($decoded -replace "\s+", " ").Trim())
}

function Normalize-Url([string]$Value) {
  $decoded = Normalize-Text $Value
  if ($decoded.StartsWith("//")) { return "https:$decoded" }
  if ($decoded.StartsWith("/")) { return "https://quantumhardstore.com$decoded" }
  return $decoded
}

function Get-CategoryProducts([string]$Url) {
  $response = Invoke-WebRequest -Uri $Url -UseBasicParsing -MaximumRedirection 5
  $html = $response.Content
  $products = New-Object System.Collections.Generic.List[object]
  $seen = New-Object "System.Collections.Generic.HashSet[string]"

  $cardPattern = '(?is)<a\b(?=[^>]*\bclass="[^"]*\bq-pcard\b[^"]*")[^>]*\bhref="([^"]+)"[^>]*\btitle="([^"]+)"'
  foreach ($match in [regex]::Matches($html, $cardPattern)) {
    $url = Normalize-Url $match.Groups[1].Value
    $title = Normalize-Text $match.Groups[2].Value
    if ($url -and $title -and $url -like "https://quantumhardstore.com/productos/*" -and $seen.Add($url)) {
      $products.Add([pscustomobject]@{ title = $title; url = $url }) | Out-Null
    }
  }

  if ($products.Count -eq 0) {
    $jsonPattern = '(?is)<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>'
    foreach ($script in [regex]::Matches($html, $jsonPattern)) {
      $raw = $script.Groups[1].Value.Trim()
      if ($raw -notmatch '"@type"\s*:\s*"Product"') { continue }
      try {
        $data = $raw | ConvertFrom-Json
        $url = ""
        if ($data.offers -and $data.offers.url) { $url = Normalize-Url $data.offers.url }
        elseif ($data.mainEntityOfPage -and $data.mainEntityOfPage.'@id') { $url = Normalize-Url $data.mainEntityOfPage.'@id' }
        $title = Normalize-Text $data.name
        if ($url -and $title -and $url -like "https://quantumhardstore.com/productos/*" -and $seen.Add($url)) {
          $products.Add([pscustomobject]@{ title = $title; url = $url }) | Out-Null
        }
      } catch {
        continue
      }
    }
  }

  return $products.ToArray()
}

function Read-State([string]$Path) {
  if (-not (Test-Path -LiteralPath $Path)) {
    return [pscustomobject]@{ seen_urls = @(); last_check = $null; category_url = $CategoryUrl }
  }
  return Get-Content -LiteralPath $Path -Raw | ConvertFrom-Json
}

function Write-State([string]$Path, [object[]]$Products) {
  $dir = Split-Path -Parent $Path
  if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
  $state = [pscustomobject]@{
    category_url = $CategoryUrl
    last_check = (Get-Date).ToString("s")
    seen_urls = @($Products | ForEach-Object { $_.url } | Sort-Object -Unique)
  }
  $state | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $Path -Encoding UTF8
}

function Write-Alert([object[]]$NewProducts, [string]$Dir) {
  if (-not (Test-Path -LiteralPath $Dir)) { New-Item -ItemType Directory -Path $Dir | Out-Null }
  $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
  $path = Join-Path $Dir "NUEVAS_GPUS_$stamp.txt"
  $lines = New-Object System.Collections.Generic.List[string]
  $lines.Add("NUEVAS GPUS DETECTADAS - $((Get-Date).ToString('yyyy-MM-dd HH:mm:ss'))") | Out-Null
  $lines.Add("") | Out-Null
  foreach ($p in $NewProducts) {
    $lines.Add($p.title) | Out-Null
    $lines.Add($p.url) | Out-Null
    $lines.Add("") | Out-Null
  }
  $lines.Add("Siguiente paso: crear descripcion con specs oficiales, publicar alias corto y entregar iframe.") | Out-Null
  $lines | Set-Content -LiteralPath $path -Encoding UTF8
  return $path
}

$products = @(Get-CategoryProducts $CategoryUrl)
if ($products.Count -eq 0) {
  Write-Output "ERROR: no se detectaron productos en la categoria."
  exit 1
}

$state = Read-State $StatePath
$known = New-Object "System.Collections.Generic.HashSet[string]"
foreach ($url in @($state.seen_urls)) {
  if ($url) { [void]$known.Add([string]$url) }
}

if ($Initialize -or $known.Count -eq 0) {
  Write-State $StatePath $products
  Write-Output "Inicializado monitor GPU. Productos actuales registrados: $($products.Count)"
  Write-Output "STATE=$StatePath"
  exit 0
}

$newProducts = @($products | Where-Object { -not $known.Contains($_.url) })
Write-State $StatePath $products

if ($newProducts.Count -gt 0) {
  $alertPath = Write-Alert $newProducts $AlertDir
  Write-Output "NUEVAS_GPUS=$($newProducts.Count)"
  foreach ($p in $newProducts) {
    Write-Output " - $($p.title)"
    Write-Output "   $($p.url)"
  }
  Write-Output "ALERT_FILE=$alertPath"
  exit 2
}

Write-Output "Sin GPUs nuevas. Productos revisados: $($products.Count)"
Write-Output "LAST_CHECK=$((Get-Date).ToString('s'))"
exit 0
