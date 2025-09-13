#!/bin/bash
# Bash монитор для Replit бота

URL="https://your-project-name.repl.co/ping"
LOG_FILE="monitor.log"

echo "🚀 Запуск мониторинга бота..."

while true; do
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "🔄 Мониторинг в $timestamp"
    
    if curl -s -o /dev/null -w "%{http_code}" $URL | grep -q "200"; then
        echo "✅ Bot ping successful at $timestamp" | tee -a $LOG_FILE
    else
        echo "⚠️ Bot ping failed at $timestamp" | tee -a $LOG_FILE
    fi
    
    sleep 300  # 5 минут
done
