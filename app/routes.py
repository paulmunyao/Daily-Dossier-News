from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "There"}
    posts = {"Welcome to the dossier a one stop place where we believe information should be available to everyone everytime at no cost"}
    return render_template("index.html", title="Home", user=user, posts=posts)
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
