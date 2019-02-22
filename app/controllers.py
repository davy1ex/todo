from flask import Blueprint, render_template


module = Blueprint('intity', __name__, url_prefix='initity')


@module.route('/')
def index():
    return render_template('initity/index.html')
