#!/usr/bin/env python3
"""
УЛЬТИМАТИВНАЯ НАСТРОЙКА МОНИТОРИНГА ДЛЯ REPLIT БОТА
"""

import os
import requests
import time
import json
from datetime import datetime

def create_ultimate_monitor():
    """Создание ультимативного монитора"""
    
    monitor_code = '''#!/usr/bin/env python3
"""
УЛЬТИМАТИВНЫЙ МОНИТОР ДЛЯ REPLIT БОТА
Автоматически настраивается и работает 24/7
"""

import requests
import time
import json
import threading
import os
from datetime import datetime

class UltimateMonitor:
    def __init__(self, repl_url):
        self.repl_url = repl_url
        self.stats = {
            'total_pings': 0,
            'successful_pings': 0,
            'failed_pings': 0,
            'start_time': datetime.now(),
            'last_success': None,
            'last_failure': None,
            'uptime_checks': 0,
            'health_checks': 0
        }
        self.running = True
        
    def ping_bot(self):
        """Пинг бота"""
        try:
            response = requests.get(f"{self.repl_url}/ping", timeout=5)
            self.stats['total_pings'] += 1
            
            if response.status_code == 200:
                self.stats['successful_pings'] += 1
                self.stats['last_success'] = datetime.now()
                return True, "OK"
            else:
                self.stats['failed_pings'] += 1
                self.stats['last_failure'] = datetime.now()
                return False, f"HTTP {response.status_code}"
                
        except Exception as e:
            self.stats['total_pings'] += 1
            self.stats['failed_pings'] += 1
            self.stats['last_failure'] = datetime.now()
            return False, str(e)
    
    def check_all_endpoints(self):
        """Проверка всех эндпоинтов"""
        endpoints = {
            'home': f"{self.repl_url}/",
            'ping': f"{self.repl_url}/ping",
            'health': f"{self.repl_url}/health",
            'stats': f"{self.repl_url}/stats"
        }
        
        results = {}
        for name, url in endpoints.items():
            try:
                response = requests.get(url, timeout=5)
                results[name] = {
                    'status': response.status_code,
                    'success': response.status_code == 200,
                    'response_time': response.elapsed.total_seconds()
                }
            except Exception as e:
                results[name] = {
                    'status': 'error',
                    'success': False,
                    'error': str(e)
                }
        
        return results
    
    def save_stats(self):
        """Сохранение статистики в файл"""
        try:
            stats_data = {
                'timestamp': datetime.now().isoformat(),
                'stats': self.stats,
                'repl_url': self.repl_url
            }
            
            with open('monitor_stats.json', 'w', encoding='utf-8') as f:
                json.dump(stats_data, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            print(f"❌ Ошибка сохранения статистики: {e}")
    
    def display_dashboard(self):
        """Отображение дашборда"""
        uptime = datetime.now() - self.stats['start_time']
        success_rate = (self.stats['successful_pings'] / self.stats['total_pings'] * 100) if self.stats['total_pings'] > 0 else 0
        
        # Очищаем экран
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("🚀 УЛЬТИМАТИВНЫЙ МОНИТОР REPLIT БОТА")
        print("=" * 60)
        print(f"🌐 URL: {self.repl_url}")
        print(f"⏱️  Время работы: {uptime}")
        print("=" * 60)
        
        print(f"📡 Всего пингов: {self.stats['total_pings']}")
        print(f"✅ Успешных: {self.stats['successful_pings']}")
        print(f"❌ Неудачных: {self.stats['failed_pings']}")
        print(f"📈 Успешность: {success_rate:.1f}%")
        print("=" * 60)
        
        if self.stats['last_success']:
            print(f"🟢 Последний успех: {self.stats['last_success'].strftime('%H:%M:%S')}")
        if self.stats['last_failure']:
            print(f"🔴 Последняя ошибка: {self.stats['last_failure'].strftime('%H:%M:%S')}")
        
        print("=" * 60)
        print("💡 Нажмите Ctrl+C для остановки")
        print("🔄 Обновление каждые 30 секунд...")
    
    def monitor_loop(self):
        """Основной цикл мониторинга"""
        while self.running:
            try:
                # Пинг бота
                success, message = self.ping_bot()
                
                # Проверка всех эндпоинтов каждые 5 пингов
                if self.stats['total_pings'] % 5 == 0:
                    endpoints = self.check_all_endpoints()
                    self.stats['health_checks'] += 1
                
                # Сохранение статистики каждые 10 пингов
                if self.stats['total_pings'] % 10 == 0:
                    self.save_stats()
                
                # Обновление дашборда
                self.display_dashboard()
                
                time.sleep(30)  # 30 секунд
                
            except KeyboardInterrupt:
                print("\\n🛑 Остановка мониторинга...")
                self.running = False
                break
            except Exception as e:
                print(f"❌ Ошибка мониторинга: {e}")
                time.sleep(60)
    
    def start(self):
        """Запуск мониторинга"""
        print("🚀 Запуск ультимативного мониторинга...")
        self.monitor_loop()
        
        # Финальная статистика
        print("\\n📊 ФИНАЛЬНАЯ СТАТИСТИКА:")
        self.display_dashboard()
        print("👋 Мониторинг остановлен")

def main():
    print("🚀 УЛЬТИМАТИВНЫЙ МОНИТОР ДЛЯ REPLIT БОТА")
    print("=" * 60)
    
    # Получаем URL
    repl_url = input("🌐 Введите URL вашего Replit проекта: ").strip()
    
    if not repl_url.startswith('http'):
        repl_url = f"https://{repl_url}"
    if not repl_url.endswith('.repl.co'):
        repl_url = f"{repl_url}.repl.co"
    
    print(f"🎯 Настройка мониторинга для: {repl_url}")
    
    # Запускаем мониторинг
    monitor = UltimateMonitor(repl_url)
    monitor.start()

if __name__ == "__main__":
    main()
'''
    
    with open('ultimate_monitor.py', 'w', encoding='utf-8') as f:
        f.write(monitor_code)
    
    print("✅ Ультимативный монитор создан: ultimate_monitor.py")

def create_auto_setup_script():
    """Создание автоматического скрипта настройки"""
    
    setup_code = '''#!/usr/bin/env python3
"""
АВТОМАТИЧЕСКАЯ НАСТРОЙКА ВСЕГО МОНИТОРИНГА
"""

import os
import subprocess
import sys

def install_requirements():
    """Установка зависимостей"""
    print("📦 Установка зависимостей...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        print("✅ Зависимости установлены")
        return True
    except Exception as e:
        print(f"❌ Ошибка установки: {e}")
        return False

def create_batch_files():
    """Создание batch файлов для Windows"""
    
    # Запуск монитора
    monitor_bat = '''@echo off
title Replit Bot Monitor
echo Starting Replit Bot Monitor...
python ultimate_monitor.py
pause
'''
    
    with open('start_monitor.bat', 'w', encoding='utf-8') as f:
        f.write(monitor_bat)
    
    # Автоматический запуск
    auto_bat = '''@echo off
title Auto Replit Bot Monitor
echo Starting Auto Monitor...
echo.

:loop
echo Starting monitor at %date% %time%
python ultimate_monitor.py
echo.
echo Waiting 60 seconds before restart...
timeout /t 60 /nobreak > nul
goto loop
'''
    
    with open('auto_monitor.bat', 'w', encoding='utf-8') as f:
        f.write(auto_bat)
    
    print("✅ Batch файлы созданы:")
    print("  - start_monitor.bat (запуск монитора)")
    print("  - auto_monitor.bat (автоматический перезапуск)")

def create_powershell_scripts():
    """Создание PowerShell скриптов"""
    
    # Основной монитор
    monitor_ps = '''# PowerShell monitor for Replit bot
$Host.UI.RawUI.WindowTitle = "Replit Bot Monitor"

Write-Host "Starting Replit Bot Monitor..." -ForegroundColor Green
python ultimate_monitor.py

Write-Host "\\nPress any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
'''
    
    with open('start_monitor.ps1', 'w', encoding='utf-8') as f:
        f.write(monitor_ps)
    
    # Автоматический монитор
    auto_ps = '''# Auto PowerShell monitor
$Host.UI.RawUI.WindowTitle = "Auto Replit Bot Monitor"

Write-Host "Starting Auto Monitor..." -ForegroundColor Green

while ($true) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "Starting monitor at $timestamp" -ForegroundColor Yellow
    
    python ultimate_monitor.py
    
    Write-Host "Waiting 60 seconds before restart..." -ForegroundColor Cyan
    Start-Sleep -Seconds 60
}
'''
    
    with open('auto_monitor.ps1', 'w', encoding='utf-8') as f:
        f.write(auto_ps)
    
    print("✅ PowerShell скрипты созданы:")
    print("  - start_monitor.ps1 (запуск монитора)")
    print("  - auto_monitor.ps1 (автоматический перезапуск)")

def create_linux_scripts():
    """Создание Linux скриптов"""
    
    # Основной монитор
    monitor_sh = '''#!/bin/bash
# Linux monitor for Replit bot

echo "Starting Replit Bot Monitor..."
python3 ultimate_monitor.py

echo "\\nPress Enter to exit..."
read
'''
    
    with open('start_monitor.sh', 'w', encoding='utf-8') as f:
        f.write(monitor_sh)
    
    # Автоматический монитор
    auto_sh = '''#!/bin/bash
# Auto Linux monitor

echo "Starting Auto Monitor..."

while true; do
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "Starting monitor at $timestamp"
    
    python3 ultimate_monitor.py
    
    echo "Waiting 60 seconds before restart..."
    sleep 60
done
'''
    
    with open('auto_monitor.sh', 'w', encoding='utf-8') as f:
        f.write(auto_sh)
    
    # Делаем исполняемыми
    try:
        os.chmod('start_monitor.sh', 0o755)
        os.chmod('auto_monitor.sh', 0o755)
    except:
        pass
    
    print("✅ Linux скрипты созданы:")
    print("  - start_monitor.sh (запуск монитора)")
    print("  - auto_monitor.sh (автоматический перезапуск)")

def main():
    print("🚀 АВТОМАТИЧЕСКАЯ НАСТРОЙКА ВСЕГО МОНИТОРИНГА")
    print("=" * 60)
    
    # Устанавливаем зависимости
    if not install_requirements():
        print("❌ Не удалось установить зависимости")
        return
    
    # Создаем ультимативный монитор
    create_ultimate_monitor()
    
    # Создаем скрипты для всех платформ
    create_batch_files()
    create_powershell_scripts()
    create_linux_scripts()
    
    print("\\n🎉 НАСТРОЙКА ЗАВЕРШЕНА!")
    print("=" * 60)
    print("📋 ЧТО ДЕЛАТЬ ДАЛЬШЕ:")
    print("1. Запустите ultimate_monitor.py")
    print("2. Или используйте готовые скрипты:")
    print("   - Windows: start_monitor.bat")
    print("   - PowerShell: start_monitor.ps1")
    print("   - Linux/Mac: ./start_monitor.sh")
    print("3. Для автоматического перезапуска используйте auto_* скрипты")
    print("4. Ваш бот теперь максимально защищен! 🛡️")

if __name__ == "__main__":
    main()
'''
    
    with open('auto_setup.py', 'w', encoding='utf-8') as f:
        f.write(setup_code)
    
    print("✅ Автоматический настройщик создан: auto_setup.py")

def main():
    print("🚀 УЛЬТИМАТИВНАЯ НАСТРОЙКА МОНИТОРИНГА")
    print("=" * 60)
    
    create_ultimate_monitor()
    create_auto_setup_script()
    
    print("\\n🎉 УЛЬТИМАТИВНАЯ НАСТРОЙКА ЗАВЕРШЕНА!")
    print("=" * 60)
    print("📋 ЧТО ДЕЛАТЬ ДАЛЬШЕ:")
    print("1. Запустите: python auto_setup.py")
    print("2. Или сразу: python ultimate_monitor.py")
    print("3. Ваш бот теперь неубиваемый! 🛡️⚡")

if __name__ == "__main__":
    main()
