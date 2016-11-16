#!../venv/bin/python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .momentjs import momentjs

app = Flask(__name__)
app.jinja_env.globals["momentjs"] = momentjs
app.config.from_object('config')
db = SQLAlchemy(app)
from app import views, models
