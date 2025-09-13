#!/usr/bin/env python3
"""
Автоматическая настройка UptimeRobot через API
"""

import requests
import json
import os

class UptimeRobotSetup:
    def __init__(self, api_key, repl_url):
        self.api_key = api_key
        self.repl_url = repl_url
        self.base_url = "https://api.uptimerobot.com/v2"
        
    def create_monitor(self):
        """Создание монитора в UptimeRobot"""
        url = f"{self.base_url}/newMonitor"
        
        data = {
            'api_key': self.api_key,
            'format': 'json',
            'type': '1',  # HTTP(s)
            'url': f"{self.repl_url}/ping",
            'friendly_name': 'German Words Bot',
            'interval': '300',  # 5 minutes
            'timeout': '30',
            'keyword_type': '0',
            'keyword_value': '',
            'http_username': '',
            'http_password': '',
            'port': '',
            'ignore_ssl_errors': '0',
            'alert_contacts': '',
            'mwindows': '',
            'custom_http_headers': '',
            'http_method': 'GET'
        }
        
        try:
            response = requests.post(url, data=data)
            result = response.json()
            
            if result['stat'] == 'ok':
                print(f"✅ Монитор создан успешно! ID: {result['monitor']['id']}")
                return True
            else:
                print(f"❌ Ошибка создания монитора: {result['error']['message']}")
                return False
                
        except Exception as e:
            print(f"❌ Ошибка API: {e}")
            return False
            
    def get_monitors(self):
        """Получение списка мониторов"""
        url = f"{self.base_url}/getMonitors"
        
        data = {
            'api_key': self.api_key,
            'format': 'json',
            'logs': '0',
            'response_times': '0',
            'response_times_average': '0',
            'response_times_start_date': '',
            'response_times_end_date': '',
            'alert_contacts': '0',
            'mwindows': '0',
            'timezone': '0',
            'custom_uptime_ratios': '',
            'custom_uptime_ranges': ''
        }
        
        try:
            response = requests.post(url, data=data)
            result = response.json()
            
            if result['stat'] == 'ok':
                print(f"📊 Найдено мониторов: {result['pagination']['total']}")
                for monitor in result['monitors']:
                    print(f"  - {monitor['friendly_name']}: {monitor['url']} (ID: {monitor['id']})")
                return result['monitors']
            else:
                print(f"❌ Ошибка получения мониторов: {result['error']['message']}")
                return []
                
        except Exception as e:
            print(f"❌ Ошибка API: {e}")
            return []

def main():
    print("🚀 АВТОМАТИЧЕСКАЯ НАСТРОЙКА UPTIMEROBOT")
    print("=" * 50)
    
    # Получаем API ключ
    api_key = os.environ.get('UPTIMEROBOT_API_KEY', '')
    if not api_key:
        print("🔑 Введите ваш API ключ UptimeRobot:")
        print("Получить можно на: https://uptimerobot.com/dashboard.php#mySettings")
        api_key = input("API Key: ").strip()
    
    # Получаем URL
    repl_url = os.environ.get('REPLIT_URL', '')
    if not repl_url:
        print("🌐 Введите URL вашего Replit проекта:")
        repl_url = input("URL: ").strip()
        if not repl_url.startswith('http'):
            repl_url = f"https://{repl_url}"
        if not repl_url.endswith('.repl.co'):
            repl_url = f"{repl_url}.repl.co"
    
    setup = UptimeRobotSetup(api_key, repl_url)
    
    # Проверяем существующие мониторы
    print("🔍 Проверяем существующие мониторы...")
    monitors = setup.get_monitors()
    
    # Проверяем, есть ли уже монитор для этого URL
    existing_monitor = None
    for monitor in monitors:
        if monitor['url'] == f"{repl_url}/ping":
            existing_monitor = monitor
            break
    
    if existing_monitor:
        print(f"✅ Монитор уже существует: {existing_monitor['friendly_name']} (ID: {existing_monitor['id']})")
    else:
        print("🆕 Создаем новый монитор...")
        if setup.create_monitor():
            print("🎉 Монитор создан успешно!")
        else:
            print("❌ Не удалось создать монитор")
    
    print("\n📋 СЛЕДУЮЩИЕ ШАГИ:")
    print("1. Проверьте дашборд UptimeRobot: https://uptimerobot.com/dashboard.php")
    print("2. Убедитесь, что монитор активен")
    print("3. Настройте уведомления при необходимости")

if __name__ == "__main__":
    main()
