from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo


class NewTaskForm(FlaskForm):
    add_task_field = StringField("Что хочешь сделать?", validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    # email = StringField("мыло", validators=[DataRequired()])
    username = StringField("никнейм", validators=[DataRequired()])
    password = PasswordField("пароль", validators=[DataRequired()])
    password1 = PasswordField("повтори пароль", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Отправить")


class LoginForm(FlaskForm):
    username = StringField("никнейм", validators=[DataRequired()])
    password = PasswordField("пароль", validators=[DataRequired()])
    remember_me = BooleanField("запомнить меня")
    submit = SubmitField("войти")
