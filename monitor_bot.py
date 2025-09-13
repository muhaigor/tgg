#!/usr/bin/env python3
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
        print(f"\n🔄 Мониторинг в {datetime.now().strftime('%H:%M:%S')}")
        
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
