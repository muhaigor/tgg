@echo off
echo 🚀 Запуск мониторинга бота...
echo.

:loop
echo 🔄 Мониторинг в %date% %time%
curl -s -o nul -w "%%{http_code}" https://your-project-name.repl.co/ping
echo.
timeout /t 300 /nobreak > nul
goto loop
