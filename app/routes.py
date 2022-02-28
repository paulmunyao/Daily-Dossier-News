from flask import render_template
from app import app
import urllib.request,json
from .request import get_latest_news


@app.route('/')
# @app.route('/index')
def index():
    user = {"username": "There"}
    posts = {"Welcome to the dossier a one stop place where we believe information should be available to everyone, everywhere and  everytime at no cost"}
    return render_template("index.html", title="Home", user=user, posts=posts)

@app.route('/news')
def news_headlines():
    # news_get = "https:newsapi.org/v2/top-headlines?country=in&apiKey=d1e7c9d92bd24e31b41ccdca38b4f31c"
    # response = urllib.request.urlopen(news_get)
    # data = response.read()
    # dict = json.loads(data)
    news_articles = get_latest_news()
    return render_template("news.html",news_articles=news_articles)    


