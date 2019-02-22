from flask import render_template
from app import create_app

app = create_app()


@app.route('/index')
def index():
    return 'hello'
    # return render_template('index.html')
