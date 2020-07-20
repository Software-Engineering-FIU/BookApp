from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm

class SignUpForm(FlaskForm):
    name_first = StringField('First Name', [validators.DataRequired()])
    name_last = StringField('Last Name', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message = 'Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Submit')
