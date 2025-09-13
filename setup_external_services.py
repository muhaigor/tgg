#!/usr/bin/env python3
"""
Автоматическая настройка внешних сервисов для мониторинга бота
"""

import requests
import json
import time
import os
from datetime import datetime

class ExternalServiceSetup:
    def __init__(self, repl_url):
        self.repl_url = repl_url
        self.services = {}
        
    def setup_uptimerobot(self):
        """Настройка UptimeRobot (требует API ключ)"""
        print("🔧 Настройка UptimeRobot...")
        
        # Инструкции для ручной настройки
        instructions = f"""
        📋 РУЧНАЯ НАСТРОЙКА UPTIMEROBOT:
        
        1. Зайдите на https://uptimerobot.com
        2. Создайте бесплатный аккаунт
        3. Нажмите "Add New Monitor"
        4. Заполните:
           - Friendly Name: German Words Bot
           - URL: {self.repl_url}/ping
           - Monitor Type: HTTP(s)
           - Monitoring Interval: 5 minutes
        5. Нажмите "Create Monitor"
        
        ✅ Готово! UptimeRobot будет пинговать ваш бот каждые 5 минут
        """
        print(instructions)
        
    def setup_statuscake(self):
        """Настройка StatusCake (требует API ключ)"""
        print("🔧 Настройка StatusCake...")
        
        instructions = f"""
        📋 РУЧНАЯ НАСТРОЙКА STATUSCAKE:
        
        1. Зайдите на https://statuscake.com
        2. Создайте бесплатный аккаунт
        3. Нажмите "Add New Test"
        4. Заполните:
           - Website Name: German Words Bot
           - Website URL: {self.repl_url}/health
           - Check Rate: 5 minutes
           - Test Type: HTTP
        5. Нажмите "Create Test"
        
        ✅ Готово! StatusCake будет проверять ваш бот каждые 5 минут
        """
        print(instructions)
        
    def setup_cron_job(self):
        """Настройка Cron-job.org"""
        print("🔧 Настройка Cron-job.org...")
        
        instructions = f"""
        📋 РУЧНАЯ НАСТРОЙКА CRON-JOB.ORG:
        
        1. Зайдите на https://cron-job.org
        2. Создайте бесплатный аккаунт
        3. Нажмите "Create Cronjob"
        4. Заполните:
           - Title: German Words Bot Ping
           - Address: {self.repl_url}/ping
           - Schedule: */5 * * * * (каждые 5 минут)
           - Timezone: Your timezone
        5. Нажмите "Create"
        
        ✅ Готово! Cron-job будет пинговать ваш бот каждые 5 минут
        """
        print(instructions)
        
    def setup_pingdom(self):
        """Настройка Pingdom"""
        print("🔧 Настройка Pingdom...")
        
        instructions = f"""
        📋 РУЧНАЯ НАСТРОЙКА PINGDOM:
        
        1. Зайдите на https://pingdom.com
        2. Создайте бесплатный аккаунт (14-дневный триал)
        3. Нажмите "Add Check"
        4. Заполните:
           - Check Name: German Words Bot
           - URL: {self.repl_url}/ping
           - Check Interval: 5 minutes
        5. Нажмите "Add Check"
        
        ✅ Готово! Pingdom будет мониторить ваш бот каждые 5 минут
        """
        print(instructions)
        
    def test_endpoints(self):
        """Тестирование эндпоинтов"""
        print("🧪 Тестирование эндпоинтов...")
        
        endpoints = [
            f"{self.repl_url}/",
            f"{self.repl_url}/ping",
            f"{self.repl_url}/health",
            f"{self.repl_url}/stats"
        ]
        
        for endpoint in endpoints:
            try:
                response = requests.get(endpoint, timeout=10)
                if response.status_code == 200:
                    print(f"✅ {endpoint} - OK ({response.status_code})")
                else:
                    print(f"⚠️ {endpoint} - {response.status_code}")
            except Exception as e:
                print(f"❌ {endpoint} - Error: {e}")
                
    def create_monitoring_script(self):
        """Создание скрипта для локального мониторинга"""
        script_content = f'''#!/usr/bin/env python3
"""
Локальный мониторинг бота
"""

import requests
import time
import json
from datetime import datetime

def monitor_bot():
    url = "{self.repl_url}"
    endpoints = ["/", "/ping", "/health", "/stats"]
    
    while True:
        print(f"\\n🔄 Мониторинг в {datetime.now().strftime('%H:%M:%S')}")
        
        for endpoint in endpoints:
            try:
                response = requests.get(url + endpoint, timeout=5)
                if response.status_code == 200:
                    print(f"✅ {{endpoint}} - OK")
                else:
                    print(f"⚠️ {{endpoint}} - {{response.status_code}}")
            except Exception as e:
                print(f"❌ {{endpoint}} - Error: {{e}}")
        
        time.sleep(300)  # Проверяем каждые 5 минут

if __name__ == "__main__":
    print("🚀 Запуск локального мониторинга...")
    monitor_bot()
'''
        
        with open('local_monitor.py', 'w', encoding='utf-8') as f:
            f.write(script_content)
        
        print("📝 Создан файл local_monitor.py для локального мониторинга")
        
    def run_setup(self):
        """Запуск полной настройки"""
        print("🚀 НАСТРОЙКА ВНЕШНИХ СЕРВИСОВ ДЛЯ МОНИТОРИНГА БОТА")
        print("=" * 60)
        print(f"🌐 URL вашего бота: {self.repl_url}")
        print("=" * 60)
        
        # Тестируем эндпоинты
        self.test_endpoints()
        print()
        
        # Настраиваем сервисы
        self.setup_uptimerobot()
        print()
        self.setup_statuscake()
        print()
        self.setup_cron_job()
        print()
        self.setup_pingdom()
        print()
        
        # Создаем локальный мониторинг
        self.create_monitoring_script()
        
        print("🎉 НАСТРОЙКА ЗАВЕРШЕНА!")
        print("=" * 60)
        print("📋 ЧТО ДЕЛАТЬ ДАЛЬШЕ:")
        print("1. Настройте все сервисы по инструкциям выше")
        print("2. Запустите local_monitor.py для локального мониторинга")
        print("3. Проверяйте статистику на https://your-repl-url.repl.co/stats")
        print("4. Ваш бот теперь защищен от сна! 🛡️")

def main():
    # Получаем URL из переменной окружения или запрашиваем у пользователя
    repl_url = os.environ.get('REPLIT_URL', '')
    
    if not repl_url:
        print("🌐 Введите URL вашего Replit проекта:")
        print("Пример: https://your-project-name.repl.co")
        repl_url = input("URL: ").strip()
        
        if not repl_url.startswith('http'):
            repl_url = f"https://{repl_url}"
            
        if not repl_url.endswith('.repl.co'):
            repl_url = f"{repl_url}.repl.co"
    
    setup = ExternalServiceSetup(repl_url)
    setup.run_setup()

if __name__ == "__main__":
    main()
