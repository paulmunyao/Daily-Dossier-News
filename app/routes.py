from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "There"}
    return '''
<html >
    <head >
        <title > Home-Page - Daily Dossier < /title >
    </head >
    <body >
        <h1 > Hi,''' + user['username'] + '''</h1>
    </body >
</html> '''
