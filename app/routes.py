from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
     user = {"username": "There"}
     return render_template("index.html",title="Home",user=user)
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
