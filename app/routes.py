from flask import render_template, flash, redirect, url_for
from app import app
from app.storynameform import LoginForm

@app.route('/')
@app.route('/startup')
def index():
     return render_template('startup.html')

@app.route('/newstory')
def newstory():
    form = LoginForm()
    return render_template('newstory.html', form=form)
