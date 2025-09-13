# PowerShell монитор для Replit бота
$url = "https://your-project-name.repl.co/ping"

while ($true) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    try {
        $response = Invoke-WebRequest -Uri $url -TimeoutSec 5
        if ($response.StatusCode -eq 200) {
            Write-Host "✅ Bot ping successful at $timestamp" -ForegroundColor Green
        } else {
            Write-Host "⚠️ Bot ping failed: $($response.StatusCode) at $timestamp" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "❌ Bot ping error: $_ at $timestamp" -ForegroundColor Red
    }
    
    Start-Sleep -Seconds 300  # 5 минут
}
