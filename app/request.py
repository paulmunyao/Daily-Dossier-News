import os
import urllib.request,json

import requests
from decouple import config

NEWS_API_KEY = config('NEWS_API_KEY')
COUNTRY = "us"


def get_latest_news():
    news_data = requests.get(
        f"https:newsapi.org/v2/top-headlines?country={COUNTRY}&apiKey={NEWS_API_KEY}").json()
    return news_data["articles"]

