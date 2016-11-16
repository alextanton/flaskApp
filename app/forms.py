from wtforms import StringField, PasswordField, SelectField, Form
from wtforms.validators import DataRequired

class MessageForm(Form):
    enter = StringField('message', validators=[DataRequired()])

class Signup(Form):
    username = StringField('name', validators=[DataRequired()])
    password = PasswordField('name', validators=[DataRequired()])
    confirm = PasswordField('name', validators=[DataRequired()])

class Login(Form):
    username = StringField('name', validators=[DataRequired()])
    password = PasswordField('name', validators=[DataRequired()])
