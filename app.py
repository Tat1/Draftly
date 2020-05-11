from flask import Flask, render_template, request

app = Flask(__name__)

#Using Jinja
@app.route('/',  methods = ['GET'])
def startup():
    return render_template('startup.html')

@app.route('/newstory', methods = ['POST'])
def newstory():
    if 'CharacternameFormControlInput' in request.args:
        # Got a character from a form...
        return render_template('newstory.html', CharacternameFormControlInput=request.args['CharacternameFormControlInput'])
    else:
        # No character yet
        return render_template('newstory.html')

@app.route('/storyparagraphs', methods = ['POST'])
def storyparagraphs():
    return render_template('storyparagraphs.html', StorynameFormControlInput=request.args['StorynameFormControlInput'], PlotlineControlSelect=request.args['PlotlineControlSelect'])

@app.route('/loadstory')
def loadstory():
    return render_template('loadstory.html')

@app.route('/charactercreation')
def charactercreation():
    return render_template('charactercreation.html')
