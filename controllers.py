from flask import render_template, redirect, request

from app import app
from app.forms import NewTaskForm
from app import db
from app.models import Task


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NewTaskForm()
    tasks = Task.query.all()
    # if form.validate_on_submit():
    if request.method == 'POST':
        if request.form['submit_button'] == '+':
            new_task = Task(body=form.add_task_field.data)
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        # elif request.form['submit_button'] == '-':
        #     return redirect('/fdgdfs')
    elif request.method == 'GET':
        return render_template('index.html', form=form, tasks=tasks)


@app.route('/del_task')
def del_task(self, id):
        db.session.delete(Task.query.filter_by(id=id).first())

        return
