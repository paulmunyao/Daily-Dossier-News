from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "There"}
    post = {"Welcome to the dossier <br> a one stop place where we believe <br> information should be available to everyone everytime at no cost"}
    return render_template("index.html", title="Home", user=user,post=post)
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
