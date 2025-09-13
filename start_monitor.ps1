# PowerShell monitor for Replit bot
$Host.UI.RawUI.WindowTitle = "Replit Bot Monitor"

Write-Host "Starting Replit Bot Monitor..." -ForegroundColor Green
python simple_monitor.py

Write-Host "Press any key to exit..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
