from flask import render_template

from app import app
from app.models import Task


tasks = []
id = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Task()
    if form.validate_on_submit():
        tasks.append(
            {
                'id': id,
                'body': add_form.new_task_field.data()
            }
        )
    return render_template('index.html', form=form)
