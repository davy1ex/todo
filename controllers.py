from flask import render_template, redirect, url_for, flash

from app import app
from app.forms import NewTaskForm
from app import db
from app.models import Task


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NewTaskForm()
    tasks = Task.query.all()
    if form.validate_on_submit():
        new_task = Task(body=form.add_task_field.data)
        db.session.add(new_task)
        db.session.commit()
        return render_template('dgdg.html')
    return render_template('index.html', form=form, tasks=tasks)
