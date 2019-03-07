from flask import render_template, redirect, url_for, flash
from flask_login import login_user, current_user
from sqlalchemy.orm import exc

from app import app
from app.forms import NewTaskForm, LoginForm, RegistrationForm
from app import db
from app.models import Task, User


@app.route("/", methods=["GET", "POST"])
def index():
    form = NewTaskForm()
    tasks = Task.query.all()
    if form.validate_on_submit(): # если поле ввода заполненно верно (читать, как "просто заполненно"")
        data_request = form.add_task_field.data

        if "+" in data_request:
            """ добавить новую задачу
            синтаксис: "+купить гараж" """
            new_task = Task(body=form.add_task_field.data[1:])
            db.session.add(new_task)
            db.session.commit()

        elif "-a" in data_request:
            """ удалить все задачи
            синтаксис: "-a" """
            db.session.query(Task).delete()
            db.session.commit()

        elif "-" in data_request:
            """ удалить задачу
            синтаксис: "-4"
            где 4 id (порядковый номер) задачи """
            try:  # ловит неверный id. Если такого нет, то страница просто перезагружается
                db.session.delete(Task.query.filter_by(id=data_request[1:]).first())
                db.session.commit()
            except exc.UnmappedInstanceError:
                pass

        return redirect(url_for("index"))

    return render_template("index.html", form=form, tasks=tasks)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Ты не зарегистирван")
            return redirect("/reg")
        login_user(user)
        return redirect(url_for("index"))
    return render_template("login.html", form=form)


@app.route("/reg", methods=["GET", "POST"])
def reg():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
        return redirect(url_for("index"))
    return render_template("registration.html", form=form)


@app.route("/logout")
def logout():
    return ""
