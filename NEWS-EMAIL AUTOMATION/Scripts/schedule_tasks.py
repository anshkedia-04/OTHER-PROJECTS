import schedule
import time
import sys
import os


# Add the root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Scripts.fetch_news import fetch_news
from Scripts.fetch_weather import fetch_weather
from Scripts.save_data import save_data
from Scripts.send_email import send_email

def daily_update():
    news = fetch_news()
    weather = fetch_weather()
    content = f"Daily Update:\n\n{news}\n\n{weather}"
    save_data(content)
    send_email("Your Daily Update", content)

# Schedule the task
schedule.every().day.at("10:10").do(daily_update)

if __name__ == "__main__":
    print("Scheduler is running...")
    while True:
        schedule.run_pending()
        time.sleep(60)
