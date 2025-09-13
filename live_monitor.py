#!/usr/bin/env python3
"""
Живой монитор для Replit бота - работает прямо сейчас!
"""

import requests
import time
import json
import threading
from datetime import datetime
import os

class LiveMonitor:
    def __init__(self, repl_url):
        self.repl_url = repl_url
        self.stats = {
            'total_pings': 0,
            'successful_pings': 0,
            'failed_pings': 0,
            'start_time': datetime.now(),
            'last_success': None,
            'last_failure': None
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
    
    def check_health(self):
        """Проверка здоровья бота"""
        try:
            response = requests.get(f"{self.repl_url}/health", timeout=5)
            if response.status_code == 200:
                data = response.json()
                return True, data
            else:
                return False, f"HTTP {response.status_code}"
        except Exception as e:
            return False, str(e)
    
    def get_stats(self):
        """Получение статистики бота"""
        try:
            response = requests.get(f"{self.repl_url}/stats", timeout=5)
            if response.status_code == 200:
                return True, response.text
            else:
                return False, f"HTTP {response.status_code}"
        except Exception as e:
            return False, str(e)
    
    def display_stats(self):
        """Отображение статистики"""
        uptime = datetime.now() - self.stats['start_time']
        success_rate = (self.stats['successful_pings'] / self.stats['total_pings'] * 100) if self.stats['total_pings'] > 0 else 0
        
        print(f"\\n📊 СТАТИСТИКА МОНИТОРИНГА:")
        print(f"⏱️  Время работы: {uptime}")
        print(f"📡 Всего пингов: {self.stats['total_pings']}")
        print(f"✅ Успешных: {self.stats['successful_pings']}")
        print(f"❌ Неудачных: {self.stats['failed_pings']}")
        print(f"📈 Успешность: {success_rate:.1f}%")
        
        if self.stats['last_success']:
            print(f"🟢 Последний успех: {self.stats['last_success'].strftime('%H:%M:%S')}")
        if self.stats['last_failure']:
            print(f"🔴 Последняя ошибка: {self.stats['last_failure'].strftime('%H:%M:%S')}")
    
    def monitor_loop(self):
        """Основной цикл мониторинга"""
        print(f"🚀 Запуск живого мониторинга для {self.repl_url}")
        print("=" * 60)
        
        while self.running:
            timestamp = datetime.now().strftime('%H:%M:%S')
            
            # Пинг бота
            success, message = self.ping_bot()
            status_icon = "✅" if success else "❌"
            print(f"{status_icon} [{timestamp}] Ping: {message}")
            
            # Проверка здоровья каждые 5 пингов
            if self.stats['total_pings'] % 5 == 0:
                health_success, health_data = self.check_health()
                if health_success:
                    print(f"🏥 [{timestamp}] Health: OK - {health_data.get('active_chats', 0)} активных чатов")
                else:
                    print(f"🏥 [{timestamp}] Health: {health_data}")
            
            # Статистика каждые 10 пингов
            if self.stats['total_pings'] % 10 == 0:
                self.display_stats()
            
            time.sleep(30)  # Пинг каждые 30 секунд
    
    def start(self):
        """Запуск мониторинга"""
        try:
            self.monitor_loop()
        except KeyboardInterrupt:
            print("\\n🛑 Остановка мониторинга...")
            self.running = False
            self.display_stats()
            print("👋 Мониторинг остановлен")

def main():
    print("🚀 ЖИВОЙ МОНИТОР ДЛЯ REPLIT БОТА")
    print("=" * 50)
    
    # Получаем URL
    repl_url = input("🌐 Введите URL вашего Replit проекта: ").strip()
    
    if not repl_url.startswith('http'):
        repl_url = f"https://{repl_url}"
    if not repl_url.endswith('.repl.co'):
        repl_url = f"{repl_url}.repl.co"
    
    print(f"🎯 Мониторинг: {repl_url}")
    print("💡 Нажмите Ctrl+C для остановки")
    print()
    
    # Запускаем мониторинг
    monitor = LiveMonitor(repl_url)
    monitor.start()

if __name__ == "__main__":
    main()
