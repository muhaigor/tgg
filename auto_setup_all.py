#!/usr/bin/env python3
"""
Автоматическая настройка всех внешних сервисов для мониторинга бота
"""

import requests
import json
import os
import time
from datetime import datetime

class AllServicesSetup:
    def __init__(self, repl_url):
        self.repl_url = repl_url
        self.results = {}
        
    def test_bot_endpoints(self):
        """Тестирование эндпоинтов бота"""
        print("🧪 Тестирование эндпоинтов бота...")
        
        endpoints = {
            'home': f"{self.repl_url}/",
            'ping': f"{self.repl_url}/ping", 
            'health': f"{self.repl_url}/health",
            'stats': f"{self.repl_url}/stats"
        }
        
        results = {}
        for name, url in endpoints.items():
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    print(f"✅ {name}: {url} - OK")
                    results[name] = True
                else:
                    print(f"⚠️ {name}: {url} - {response.status_code}")
                    results[name] = False
            except Exception as e:
                print(f"❌ {name}: {url} - Error: {e}")
                results[name] = False
                
        return results
        
    def setup_uptimerobot_api(self):
        """Настройка UptimeRobot через API"""
        print("\n🔧 Настройка UptimeRobot через API...")
        
        api_key = os.environ.get('UPTIMEROBOT_API_KEY', '')
        if not api_key:
            print("⚠️ API ключ UptimeRobot не найден в переменных окружения")
            print("   Установите UPTIMEROBOT_API_KEY или настройте вручную")
            return False
            
        url = "https://api.uptimerobot.com/v2/newMonitor"
        data = {
            'api_key': api_key,
            'format': 'json',
            'type': '1',
            'url': f"{self.repl_url}/ping",
            'friendly_name': 'German Words Bot',
            'interval': '300',
            'timeout': '30'
        }
        
        try:
            response = requests.post(url, data=data)
            result = response.json()
            
            if result['stat'] == 'ok':
                print(f"✅ UptimeRobot монитор создан! ID: {result['monitor']['id']}")
                return True
            else:
                print(f"❌ Ошибка UptimeRobot: {result['error']['message']}")
                return False
        except Exception as e:
            print(f"❌ Ошибка API UptimeRobot: {e}")
            return False
            
    def create_webhook_monitor(self):
        """Создание веб-хука для мониторинга"""
        print("\n🔧 Создание веб-хука для мониторинга...")
        
        webhook_content = f'''#!/usr/bin/env python3
"""
Веб-хук для мониторинга бота
"""

import requests
import time
import json
from datetime import datetime

def ping_bot():
    url = "{self.repl_url}/ping"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ Bot ping successful at {{datetime.now()}}")
            return True
        else:
            print(f"⚠️ Bot ping failed: {{response.status_code}}")
            return False
    except Exception as e:
        print(f"❌ Bot ping error: {{e}}")
        return False

if __name__ == "__main__":
    ping_bot()
'''
        
        with open('webhook_monitor.py', 'w', encoding='utf-8') as f:
            f.write(webhook_content)
            
        print("✅ Веб-хук создан: webhook_monitor.py")
        return True
        
    def create_cron_script(self):
        """Создание скрипта для cron"""
        print("\n🔧 Создание скрипта для cron...")
        
        cron_script = f'''#!/bin/bash
# Cron скрипт для мониторинга бота
# Добавьте в crontab: */5 * * * * /path/to/cron_monitor.sh

URL="{self.repl_url}/ping"
LOG_FILE="cron_monitor.log"

echo "$(date): Pinging bot..." >> $LOG_FILE
curl -s -o /dev/null -w "%{{http_code}}" $URL >> $LOG_FILE
echo "" >> $LOG_FILE
'''
        
        with open('cron_monitor.sh', 'w') as f:
            f.write(cron_script)
            
        # Делаем скрипт исполняемым
        os.chmod('cron_monitor.sh', 0o755)
        
        print("✅ Cron скрипт создан: cron_monitor.sh")
        return True
        
    def create_powershell_script(self):
        """Создание PowerShell скрипта для Windows"""
        print("\n🔧 Создание PowerShell скрипта...")
        
        ps_script = f'''# PowerShell скрипт для мониторинга бота
# Запустите: .\\monitor_bot.ps1

$url = "{self.repl_url}/ping"
$logFile = "monitor_bot.log"

while ($true) {{
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    try {{
        $response = Invoke-WebRequest -Uri $url -TimeoutSec 5
        if ($response.StatusCode -eq 200) {{
            Write-Host "✅ Bot ping successful at $timestamp"
            Add-Content -Path $logFile -Value "$timestamp: SUCCESS"
        }} else {{
            Write-Host "⚠️ Bot ping failed: $($response.StatusCode)"
            Add-Content -Path $logFile -Value "$timestamp: FAILED - $($response.StatusCode)"
        }}
    }} catch {{
        Write-Host "❌ Bot ping error: $_"
        Add-Content -Path $logFile -Value "$timestamp: ERROR - $_"
    }}
    
    Start-Sleep -Seconds 300  # 5 минут
}}
'''
        
        with open('monitor_bot.ps1', 'w', encoding='utf-8') as f:
            f.write(ps_script)
            
        print("✅ PowerShell скрипт создан: monitor_bot.ps1")
        return True
        
    def create_docker_monitor(self):
        """Создание Docker контейнера для мониторинга"""
        print("\n🔧 Создание Docker монитора...")
        
        dockerfile = '''FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY monitor.py .

CMD ["python", "monitor.py"]
'''
        
        monitor_py = f'''#!/usr/bin/env python3
"""
Docker контейнер для мониторинга бота
"""

import requests
import time
import json
from datetime import datetime

def monitor_bot():
    url = "{self.repl_url}/ping"
    
    while True:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"✅ Bot ping successful at {{datetime.now()}}")
            else:
                print(f"⚠️ Bot ping failed: {{response.status_code}}")
        except Exception as e:
            print(f"❌ Bot ping error: {{e}}")
        
        time.sleep(300)  # 5 минут

if __name__ == "__main__":
    print("🚀 Starting bot monitor...")
    monitor_bot()
'''
        
        with open('Dockerfile.monitor', 'w') as f:
            f.write(dockerfile)
            
        with open('monitor.py', 'w', encoding='utf-8') as f:
            f.write(monitor_py)
            
        print("✅ Docker монитор создан: Dockerfile.monitor, monitor.py")
        return True
        
    def generate_setup_instructions(self):
        """Генерация инструкций по настройке"""
        print("\n📋 Генерация инструкций...")
        
        instructions = f"""
# 🚀 ИНСТРУКЦИИ ПО НАСТРОЙКЕ МОНИТОРИНГА

## 🌐 URL вашего бота: {self.repl_url}

## 🔧 Автоматические скрипты созданы:

### 1. Python монитор
```bash
python webhook_monitor.py
```

### 2. Cron монитор (Linux/Mac)
```bash
chmod +x cron_monitor.sh
# Добавьте в crontab: */5 * * * * /path/to/cron_monitor.sh
```

### 3. PowerShell монитор (Windows)
```powershell
.\\monitor_bot.ps1
```

### 4. Docker монитор
```bash
docker build -f Dockerfile.monitor -t bot-monitor .
docker run -d --name bot-monitor bot-monitor
```

## 🌐 Внешние сервисы (настройте вручную):

### UptimeRobot
1. https://uptimerobot.com
2. URL: {self.repl_url}/ping
3. Interval: 5 minutes

### StatusCake  
1. https://statuscake.com
2. URL: {self.repl_url}/health
3. Interval: 5 minutes

### Cron-job.org
1. https://cron-job.org
2. URL: {self.repl_url}/ping
3. Schedule: */5 * * * *

## 📊 Мониторинг:
- Статистика: {self.repl_url}/stats
- Health check: {self.repl_url}/health
- Ping: {self.repl_url}/ping

## 🎯 Результат:
Ваш бот теперь защищен от сна множественными механизмами!
"""
        
        with open('SETUP_INSTRUCTIONS.md', 'w', encoding='utf-8') as f:
            f.write(instructions)
            
        print("✅ Инструкции созданы: SETUP_INSTRUCTIONS.md")
        return True
        
    def run_full_setup(self):
        """Запуск полной настройки"""
        print("🚀 ПОЛНАЯ АВТОМАТИЧЕСКАЯ НАСТРОЙКА МОНИТОРИНГА")
        print("=" * 60)
        print(f"🌐 URL бота: {self.repl_url}")
        print("=" * 60)
        
        # Тестируем бота
        endpoint_results = self.test_bot_endpoints()
        
        # Настраиваем UptimeRobot
        uptimerobot_result = self.setup_uptimerobot_api()
        
        # Создаем скрипты
        webhook_result = self.create_webhook_monitor()
        cron_result = self.create_cron_script()
        ps_result = self.create_powershell_script()
        docker_result = self.create_docker_monitor()
        
        # Генерируем инструкции
        instructions_result = self.generate_setup_instructions()
        
        # Результаты
        self.results = {
            'endpoints': endpoint_results,
            'uptimerobot': uptimerobot_result,
            'webhook': webhook_result,
            'cron': cron_result,
            'powershell': ps_result,
            'docker': docker_result,
            'instructions': instructions_result
        }
        
        print("\n🎉 НАСТРОЙКА ЗАВЕРШЕНА!")
        print("=" * 60)
        print("📊 РЕЗУЛЬТАТЫ:")
        for service, result in self.results.items():
            status = "✅" if result else "❌"
            print(f"{status} {service.upper()}")
        
        print("\n📋 СЛЕДУЮЩИЕ ШАГИ:")
        print("1. Прочитайте SETUP_INSTRUCTIONS.md")
        print("2. Настройте внешние сервисы по инструкциям")
        print("3. Запустите один из созданных скриптов мониторинга")
        print("4. Ваш бот теперь максимально защищен! 🛡️")

def main():
    # Получаем URL
    repl_url = os.environ.get('REPLIT_URL', '')
    if not repl_url:
        print("🌐 Введите URL вашего Replit проекта:")
        print("Пример: https://your-project-name.repl.co")
        repl_url = input("URL: ").strip()
        
        if not repl_url.startswith('http'):
            repl_url = f"https://{repl_url}"
        if not repl_url.endswith('.repl.co'):
            repl_url = f"{repl_url}.repl.co"
    
    setup = AllServicesSetup(repl_url)
    setup.run_full_setup()

if __name__ == "__main__":
    main()
