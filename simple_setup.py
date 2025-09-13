#!/usr/bin/env python3
"""
Простая настройка мониторинга для Replit бота
"""

import os
import requests
import time
from datetime import datetime

def create_simple_monitor():
    """Создание простого монитора"""
    
    monitor_code = '''#!/usr/bin/env python3
"""
Простой монитор для Replit бота
"""

import requests
import time
from datetime import datetime

def monitor_bot(repl_url):
    """Мониторинг бота"""
    print(f"🚀 Запуск мониторинга для {repl_url}")
    print("💡 Нажмите Ctrl+C для остановки")
    print("=" * 50)
    
    ping_count = 0
    success_count = 0
    
    while True:
        try:
            ping_count += 1
            timestamp = datetime.now().strftime('%H:%M:%S')
            
            # Пинг бота
            response = requests.get(f"{repl_url}/ping", timeout=5)
            
            if response.status_code == 200:
                success_count += 1
                status = "✅ OK"
            else:
                status = f"⚠️ {response.status_code}"
            
            success_rate = (success_count / ping_count * 100) if ping_count > 0 else 0
            
            print(f"[{timestamp}] Ping #{ping_count}: {status} | Успешность: {success_rate:.1f}%")
            
            # Проверка здоровья каждые 5 пингов
            if ping_count % 5 == 0:
                try:
                    health_response = requests.get(f"{repl_url}/health", timeout=5)
                    if health_response.status_code == 200:
                        health_data = health_response.json()
                        active_chats = health_data.get('active_chats', 0)
                        print(f"🏥 Health check: {active_chats} активных чатов")
                except:
                    print("🏥 Health check: ошибка")
            
            time.sleep(30)  # 30 секунд
            
        except KeyboardInterrupt:
            print("\\n🛑 Остановка мониторинга...")
            print(f"📊 Итого пингов: {ping_count}, успешных: {success_count}")
            break
        except Exception as e:
            print(f"❌ Ошибка: {e}")
            time.sleep(60)

if __name__ == "__main__":
    # Замените на ваш URL
    REPL_URL = "https://your-project-name.repl.co"
    print("🌐 Введите URL вашего Replit проекта:")
    repl_url = input("URL: ").strip()
    
    if not repl_url.startswith('http'):
        repl_url = f"https://{repl_url}"
    if not repl_url.endswith('.repl.co'):
        repl_url = f"{repl_url}.repl.co"
    
    monitor_bot(repl_url)
'''
    
    with open('simple_monitor.py', 'w', encoding='utf-8') as f:
        f.write(monitor_code)
    
    print("✅ Простой монитор создан: simple_monitor.py")

def create_batch_file():
    """Создание batch файла для Windows"""
    
    batch_content = '''@echo off
title Replit Bot Monitor
echo Starting Replit Bot Monitor...
python simple_monitor.py
pause
'''
    
    with open('start_monitor.bat', 'w', encoding='utf-8') as f:
        f.write(batch_content)
    
    print("✅ Batch файл создан: start_monitor.bat")

def create_powershell_script():
    """Создание PowerShell скрипта"""
    
    ps_content = '''# PowerShell monitor for Replit bot
$Host.UI.RawUI.WindowTitle = "Replit Bot Monitor"

Write-Host "Starting Replit Bot Monitor..." -ForegroundColor Green
python simple_monitor.py

Write-Host "Press any key to exit..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
'''
    
    with open('start_monitor.ps1', 'w', encoding='utf-8') as f:
        f.write(ps_content)
    
    print("✅ PowerShell скрипт создан: start_monitor.ps1")

def create_instructions():
    """Создание инструкций"""
    
    instructions = '''# 🚀 ПРОСТАЯ НАСТРОЙКА МОНИТОРИНГА

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

## 🔧 Созданные скрипты:

### 1. Python монитор
```bash
python simple_monitor.py
```

### 2. Windows Batch
```cmd
start_monitor.bat
```

### 3. PowerShell
```powershell
.\\start_monitor.ps1
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

1. **Запустите один из скриптов** мониторинга
2. **Настройте внешние сервисы** по инструкциям выше
3. **Проверьте веб-интерфейс** бота

**Ваш бот теперь максимально защищен от сна! 🛡️⚡**
'''
    
    with open('SIMPLE_SETUP.md', 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print("✅ Инструкции созданы: SIMPLE_SETUP.md")

def main():
    print("🚀 ПРОСТАЯ НАСТРОЙКА МОНИТОРИНГА")
    print("=" * 50)
    
    create_simple_monitor()
    create_batch_file()
    create_powershell_script()
    create_instructions()
    
    print("\\n🎉 НАСТРОЙКА ЗАВЕРШЕНА!")
    print("=" * 50)
    print("📋 ЧТО ДЕЛАТЬ ДАЛЬШЕ:")
    print("1. Прочитайте SIMPLE_SETUP.md")
    print("2. Запустите: python simple_monitor.py")
    print("3. Или используйте готовые скрипты:")
    print("   - Windows: start_monitor.bat")
    print("   - PowerShell: start_monitor.ps1")
    print("4. Настройте внешние сервисы")
    print("5. Ваш бот теперь неубиваемый! 🛡️")

if __name__ == "__main__":
    main()
