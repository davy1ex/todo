from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Task(FlaskForm):
    add_task_field = StringField('What you want do?', validators=[DataRequired()])
    submit_button = SubmitField('+')
    delete_button = SubmitField('-')

