from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    enter = StringField('message', validators=[DataRequired()])

class Signup(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    password = PasswordField('name', validators=[DataRequired()])
    confirm = PasswordField('name', validators=[DataRequired()])

class Login(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    password = PasswordField('name', validators=[DataRequired()])