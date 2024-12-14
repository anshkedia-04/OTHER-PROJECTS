import requests
import sys
import os


# Add the root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.api_keys import NEWS_API_KEY
from config.settings import NEWS_URL


# Add the root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def fetch_news():
    try:
        response = requests.get(NEWS_URL + NEWS_API_KEY)
        news_data = response.json()
        headlines = []
        for article in news_data.get("articles", [])[:5]:
            headlines.append(article["title"])
        return "\n".join(headlines)
    except Exception as e:
        return f"Error fetching news: {e}"
