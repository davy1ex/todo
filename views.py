# Сделать:
# -- нормальное айди


from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, login_required, logout_user
from sqlalchemy.orm import exc
from werkzeug.urls import url_parse

from app import app
from app.forms import NewTaskForm, LoginForm, RegistrationForm
from app import db
from app.models import Task, User


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    form = NewTaskForm()
    user = User.query.filter_by(username=current_user.username).first()
    tasks = Task.query.filter_by(master=user).all()
    if form.validate_on_submit(): # если поле ввода заполненно верно (читать, как "просто заполненно"")
        data_request = form.add_task_field.data

        if "+" in data_request:
            """ добавить новую задачу
            синтаксис: "+купить гараж" """
            new_task = Task(body=form.add_task_field.data[1:], master=user, self_id=len(tasks)+1)
            db.session.add(new_task)
            db.session.commit()

        elif "-a" in data_request:
            """ удалить все задачи
            синтаксис: "-a" """
            db.session.query(Task).filter_by(master=user).delete()
            db.session.commit()

        elif "-" in data_request:
            """ удалить задачу
            синтаксис: "-4"
            где 4 id (порядковый номер) задачи """
            try:  # ловит неверный id. Если такого нет, то страница просто перезагружается
                db.session.delete(Task.query.filter_by(id=data_request[1:], master=user).first())
                db.session.commit()
            except exc.UnmappedInstanceError:
                pass

        return redirect(url_for("index"))

    return render_template("index.html", form=form, tasks=tasks, title="main")


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
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(url_for("index"))
    return render_template("login.html", form=form, title="login")


@app.route("/reg", methods=["GET", "POST"])
def reg():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("index"))
    return render_template("registration.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
