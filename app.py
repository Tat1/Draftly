from flask import Flask, render_template, request

app = Flask(__name__)

theCharacters = []
theOvercoming = []

#Using Jinja
@app.route('/',  methods = ['GET'])
def startup():
    return render_template('startup.html')

@app.route('/newstory', methods = ['POST'])
def newstory():
    AnticipationName = request.form["PlotlineControlSelect"]
    DreamName = request.form["PlotlineControlSelect"]
    FrustrationName = request.form["PlotlineControlSelect"]
    NightmareName = request.form["PlotlineControlSelect"]
    MiraculousEscapeName = request.form["PlotlineControlSelect"]
        # Store as a Python dictionary:
    theOvercoming.append({'anticipation' : AnticipationName,
                          'dream' : DreamName,
                          'frustration' : FrustrationName,
                          'nightmare' : NightmareName,
                          'miraculous escape' : MiraculousEscapeName,
                         })

    return render_template('newstory.html',PlotlineControlSelect=request.form['PlotlineControlSelect'], characters=theCharacters, overcoming=theOvercoming)

@app.route('/storyparagraphs', methods = ['POST'])
def storyparagraphs():
    return render_template('storyparagraphs.html', StorynameFormControlInput=request.form['StorynameFormControlInput'], PlotlineControlSelect=request.form['PlotlineControlSelect'], characters=theCharacters, overcoming=theOvercoming)


@app.route('/loadstory')
def loadstory():
    return render_template('loadstory.html')

@app.route('/charactercreation', methods = ['POST'])
def charactercreation():
    charName = request.form["CharacterFormControl"]
    roleName = request.form["RoleControlSelect"]
    archetypeName = request.form["ArchetypeControlSelect"]

    # Store as a Python dictionary:
    theCharacters.append({'name' : charName,
                          'role' : roleName,
                          'arche' : archetypeName})

    return render_template('newstory.html', characters=theCharacters)



