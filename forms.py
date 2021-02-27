from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SignUpForm(FlaskForm):
    item = StringField('')
    submit = SubmitField('Submit')