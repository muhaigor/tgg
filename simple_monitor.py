#!/usr/bin/env python3
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
            print("\n🛑 Остановка мониторинга...")
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
