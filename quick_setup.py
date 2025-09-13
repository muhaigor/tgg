#!/usr/bin/env python3
"""
Быстрая настройка мониторинга для любого Replit проекта
"""

import os
import requests
from datetime import datetime

def create_monitoring_scripts():
    """Создание всех необходимых скриптов мониторинга"""
    
    print("🚀 Создание скриптов мониторинга...")
    
    # 1. Python монитор
    python_monitor = '''#!/usr/bin/env python3
"""
Универсальный монитор для Replit бота
"""

import requests
import time
import json
from datetime import datetime

def monitor_bot(repl_url):
    """Мониторинг бота"""
    endpoints = {
        'home': f"{repl_url}/",
        'ping': f"{repl_url}/ping",
        'health': f"{repl_url}/health",
        'stats': f"{repl_url}/stats"
    }
    
    while True:
        print(f"\\n🔄 Мониторинг в {datetime.now().strftime('%H:%M:%S')}")
        
        for name, url in endpoints.items():
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    print(f"✅ {name}: OK")
                else:
                    print(f"⚠️ {name}: {response.status_code}")
            except Exception as e:
                print(f"❌ {name}: Error - {e}")
        
        time.sleep(300)  # 5 минут

if __name__ == "__main__":
    # Замените на ваш URL
    REPL_URL = "https://your-project-name.repl.co"
    print(f"🚀 Запуск мониторинга для {REPL_URL}")
    monitor_bot(REPL_URL)
'''
    
    with open('monitor_bot.py', 'w', encoding='utf-8') as f:
        f.write(python_monitor)
    
    # 2. Batch файл для Windows
    batch_monitor = '''@echo off
echo 🚀 Запуск мониторинга бота...
echo.

:loop
echo 🔄 Мониторинг в %date% %time%
curl -s -o nul -w "%%{http_code}" https://your-project-name.repl.co/ping
echo.
timeout /t 300 /nobreak > nul
goto loop
'''
    
    with open('monitor_bot.bat', 'w', encoding='utf-8') as f:
        f.write(batch_monitor)
    
    # 3. PowerShell скрипт
    ps_monitor = '''# PowerShell монитор для Replit бота
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
'''
    
    with open('monitor_bot.ps1', 'w', encoding='utf-8') as f:
        f.write(ps_monitor)
    
    # 4. Bash скрипт для Linux/Mac
    bash_monitor = '''#!/bin/bash
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
'''
    
    with open('monitor_bot.sh', 'w', encoding='utf-8') as f:
        f.write(bash_monitor)
    
    # Делаем bash скрипт исполняемым
    try:
        os.chmod('monitor_bot.sh', 0o755)
    except:
        pass
    
    print("✅ Скрипты мониторинга созданы:")
    print("  - monitor_bot.py (Python)")
    print("  - monitor_bot.bat (Windows Batch)")
    print("  - monitor_bot.ps1 (PowerShell)")
    print("  - monitor_bot.sh (Bash)")

def create_setup_guide():
    """Создание руководства по настройке"""
    
    guide = '''# 🚀 РУКОВОДСТВО ПО НАСТРОЙКЕ МОНИТОРИНГА

## 📋 Что уже настроено в боте:

✅ **Множественные механизмы активности:**
- Поток активности каждые 30 секунд
- Keep-alive задача каждые 2 минуты
- Частый пинг каждые 30 секунд
- Логирование активности в файл
- Flask веб-сервер с эндпоинтами

✅ **Веб-интерфейс:**
- `/` - главная страница с статистикой
- `/ping` - простой пинг
- `/health` - проверка здоровья
- `/stats` - подробная статистика

## 🔧 Дополнительные скрипты созданы:

### 1. Python монитор
```bash
# Отредактируйте URL в файле, затем:
python monitor_bot.py
```

### 2. Windows Batch
```cmd
# Отредактируйте URL в файле, затем:
monitor_bot.bat
```

### 3. PowerShell
```powershell
# Отредактируйте URL в файле, затем:
.\\monitor_bot.ps1
```

### 4. Bash (Linux/Mac)
```bash
# Отредактируйте URL в файле, затем:
./monitor_bot.sh
```

## 🌐 Внешние сервисы (настройте вручную):

### 1. UptimeRobot (БЕСПЛАТНО)
1. Зайдите на https://uptimerobot.com
2. Создайте аккаунт
3. Добавьте новый монитор:
   - **URL**: `https://your-project-name.repl.co/ping`
   - **Type**: HTTP(s)
   - **Interval**: 5 minutes

### 2. StatusCake (БЕСПЛАТНО)
1. Зайдите на https://statuscake.com
2. Создайте аккаунт
3. Добавьте новый тест:
   - **URL**: `https://your-project-name.repl.co/health`
   - **Check Rate**: 5 minutes

### 3. Cron-job.org (БЕСПЛАТНО)
1. Зайдите на https://cron-job.org
2. Создайте аккаунт
3. Добавьте новую задачу:
   - **URL**: `https://your-project-name.repl.co/ping`
   - **Schedule**: `*/5 * * * *` (каждые 5 минут)

### 4. Pingdom (14-дневный триал)
1. Зайдите на https://pingdom.com
2. Создайте аккаунт
3. Добавьте новый чек:
   - **URL**: `https://your-project-name.repl.co/ping`
   - **Interval**: 5 minutes

## 📊 Мониторинг:

### Проверьте работу бота:
- **Главная страница**: `https://your-project-name.repl.co`
- **Статистика**: `https://your-project-name.repl.co/stats`
- **Health check**: `https://your-project-name.repl.co/health`
- **Ping**: `https://your-project-name.repl.co/ping`

## 🎯 Результат:

С этими настройками ваш бот будет:
- ✅ Создавать активность каждые 30 секунд
- ✅ Получать внешние пинги каждые 5 минут
- ✅ Иметь множественные механизмы защиты
- ✅ Логировать всю активность
- ✅ Предоставлять веб-интерфейс для мониторинга

## 🚀 Быстрый старт:

1. **Отредактируйте URL** во всех созданных скриптах
2. **Запустите один из скриптов** мониторинга
3. **Настройте внешние сервисы** по инструкциям выше
4. **Проверьте веб-интерфейс** бота

**Ваш бот теперь максимально защищен от сна! 🛡️⚡**
'''
    
    with open('MONITORING_GUIDE.md', 'w', encoding='utf-8') as f:
        f.write(guide)
    
    print("✅ Руководство создано: MONITORING_GUIDE.md")

def main():
    print("🚀 БЫСТРАЯ НАСТРОЙКА МОНИТОРИНГА")
    print("=" * 50)
    
    create_monitoring_scripts()
    print()
    create_setup_guide()
    
    print("\n🎉 НАСТРОЙКА ЗАВЕРШЕНА!")
    print("=" * 50)
    print("📋 ЧТО ДЕЛАТЬ ДАЛЬШЕ:")
    print("1. Прочитайте MONITORING_GUIDE.md")
    print("2. Отредактируйте URL во всех скриптах")
    print("3. Запустите один из скриптов мониторинга")
    print("4. Настройте внешние сервисы")
    print("5. Ваш бот теперь неубиваемый! 🛡️")

if __name__ == "__main__":
    main()
