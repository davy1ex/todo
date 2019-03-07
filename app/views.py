from flask import render_template, redirect

from app import app
from app.forms import NewTaskForm
from app import db
from app.models import Task
from sqlalchemy.orm import exc


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NewTaskForm()
    tasks = Task.query.all()
    if form.validate_on_submit(): # если поле ввода заполненно верно (читать, как "просто заполненно"")
        data_request = form.add_task_field.data

        if '+' in data_request:
            """ добавить новую задачу
            синтаксис: "+купить гараж" """
            new_task = Task(body=form.add_task_field.data[1:])
            db.session.add(new_task)
            db.session.commit()

        elif '-a' in data_request:
            """ удалить все задачи
            синтаксис: "-a" """
            db.session.query(Task).delete()
            db.session.commit()

        elif '-' in data_request:
            """ удалить задачу
            синтаксис: "-4"
            где 4 id (порядковый номер) задачи """
            try:  # ловит неверный id. Если такого нет, то страница просто перезагружается
                db.session.delete(Task.query.filter_by(id=data_request[1:]).first())
                db.session.commit()
            except exc.UnmappedInstanceError:
                pass

        return redirect('/')

    return render_template('index.html', form=form, tasks=tasks)
