from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewTaskForm(FlaskForm):
    add_task_field = StringField('What you want do?')
    submit_button = SubmitField('+')
    delete_button = SubmitField('-')

