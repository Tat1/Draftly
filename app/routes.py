from flask import render_template, flash, redirect, url_for
from app import app
from app.storynameform import LoginForm
from flask_login import current_user, login_user

@app.route('/')

#@app.route('/login', methods=['GET', 'POST'])
#def login():
    #if current_user.is_authenticated:
        #return redirect(url_for('index'))
    #form = LoginForm()
    #if form.validate_on_submit():
        #if user is None or not user.check_password(form.password.data):
            #flash('Invalid username or password')
            #return redirect(url_for('login'))
        #login_user(user, remember=form.remember_me.data)
        #return redirect('/index')
    #return render_template('login.html', title='Sign In', form=form)



@app.route('/startup')
def index():
     return render_template('startup.html')

#@app.route('/newstory')
#def newstory():
    #return render_template('newstory.html')

#@app.route('/loadstory')
#def index():
     #return render_template('loadstory.html')
    
#@app.route('/charactercreation')
#def index():
     #return render_template('charactercreation.html')