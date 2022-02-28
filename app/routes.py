from flask import render_template
from app import app
import urllib.request,json
from .request import get_latest_news


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "There"}
    posts = {"Welcome to the dossier a one stop place where we believe information should be available to everyone, everywhere and  everytime at no cost"}
    return render_template("index.html", title="Home", user=user, posts=posts)

@app.route('/news')
def get_news():
    news_get = "https:newsapi.org/v2/top-headlines?country=in&apiKey=d1e7c9d92bd24e31b41ccdca38b4f31c"
    response = urllib.request.urlopen(news_get)
    data = response.read()
    dict = json.loads(data)
    return render_template("index.html",news=dict["articles"])    

        
    '''
<html >
    <head >
        <title > Home-Page - Daily Dossier < /title >
    </head >
    <body >
        <h1 > Hi," + user['username'] + "</h1>
    </body >
</html> 
    '''
