from __future__ import print_function # In python 2.7
import sys
from app import app, db, models
from flask import render_template, request, redirect, session, make_response
from .forms import MessageForm, Signup, Login
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    print(datetime.utcnow(), file=sys.stderr)
    return render_template("index.html", time=datetime.utcnow())

@app.route('/message', methods=['GET', 'POST'])
def message():
    if(request.method == "POST"):
        message = request.form["enter"]
        id = models.User.query.filter_by(username=session["user"]).first().id
        message = models.Message(body=message, timestamp=datetime.utcnow(), user_id=id)
        db.session.add(message)
        db.session.commit()
        form = MessageForm()
        messages = models.Message.query.all()
        return render_template("message.html", title='Home', form=form, messages=messages)
    if(session["user"]):
        messages = models.Message.query.all()
        form = MessageForm()
        return render_template("message.html", title='Home', form=form, messages=messages)
    else:
        return redirect('/')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Signup(request.form)
    if(request.method == 'POST'):
        if(request.form["password"] == request.form["confirm"] and form.validate()):
            user = models.User(
                username = request.form["username"],
                password = request.form["password"]
            )
            db.session.add(user)
            db.session.commit()
            session["user"] = request.form["username"]
            redirect("/index.html")
            return render_template("index.html", time=datetime.utcnow())
            #print("g", file=sys.stderr)
        else:
            form = Signup()
            response = make_response(render_template('signup.html', error=True, form=form))
            return response
    form = Signup()
    return render_template("signup.html", form=form, error=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login(request.form)
    if(request.method == 'POST'):
        if(form.validate()):
            user = request.form["username"]
            password = request.form["password"]
            user = models.User.query.filter_by(username=user).first()
            if(user.password == password):
                session["user"] = user.username
            return redirect('/')
        else:
            form = Login()
            response = make_response(render_template('login.html', error=True, form=form))
            return response
    form = Signup()
    return render_template("login.html", form=form, error=False)

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.clear()
    return redirect('/')