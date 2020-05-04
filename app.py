from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def startup():
    return render_template('startup.html')

@app.route('/about')
def about():
    return 'This is a url shortener'