from flask import Flask, render_template, request

app = Flask(__name__)

theCharacters = []
theRoles = []
theArchetypes = []

#Using Jinja
@app.route('/',  methods = ['GET'])
def startup():
    return render_template('startup.html')

@app.route('/newstory', methods = ['POST'])
def newstory():
    return render_template('newstory.html', characters=theCharacters, roles=theRoles, archetypes=theArchetypes)

@app.route('/storyparagraphs', methods = ['POST'])
def storyparagraphs():
    return render_template('storyparagraphs.html', StorynameFormControlInput=request.form['StorynameFormControlInput'], PlotlineControlSelect=request.form['PlotlineControlSelect'])

@app.route('/loadstory')
def loadstory():
    return render_template('loadstory.html')

@app.route('/charactercreation', methods = ['POST'])
def charactercreation():
    charName = request.form["CharacterFormControl"]
    theCharacters.append(charName)
    roleName = request.form["RoleControlSelect"]
    theRoles.append(roleName)
    archetypeName = request.form["ArchetypeControlSelect"]
    theArchetypes.append(archetypeName)

    return render_template('newstory.html', characters=theCharacters, roles=theRoles, archetypes=theArchetypes)
