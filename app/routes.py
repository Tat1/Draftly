from flask import render_template, flash, redirect, url_for
from app import app
from app.storynameform import LoginForm

@app.route('/')

@app.route('/startup')
def startup():
     return render_template('startup.html')

@app.route('/newstory')
def newstory():
    return render_template('newstory.html')

@app.route('/loadstory')
def loadstory():
     return render_template('loadstory.html')
    
@app.route('/charactercreation')
def charactercreation():
     return render_template('charactercreation.html')