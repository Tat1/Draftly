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

    return render_template('newstory.html', characters=theCharacters, overcoming=theOvercoming)

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


#1 Overcoming The Monster
#ed_user = Phase(name='Anticipation')
#ed_user = Phase(name='Dream')
#ed_user = Phase(name='Frustration')
#ed_user = Phase(name='Nightmare')
#ed_user = Phase(name='Miraculous Escape')

#2 Rags to Riches
#ed_user = Phase(name='Initial Wretchedness then Call to Action')
#ed_user = Phase(name='Getting out into the World')
#ed_user = Phase(name='Central Crisis')
#ed_user = Phase(name='Independence and Ordeal')
#ed_user = Phase(name='Fulfillment')

#3 Quest
#ed_user = Phase(name='The Call')
#ed_user = Phase(name='The Journey')
#ed_user = Phase(name='Arrival and Frustration')
#ed_user = Phase(name='Final Ordeal')
#ed_user = Phase(name='The Goal')


#4 Voyage and Return
#ed_user = Phase(name='Anticipation Stage and Fall into Another World')
#ed_user = Phase(name='Initial Fascination or Dream Stage')
#ed_user = Phase(name='Frustration')
#ed_user = Phase(name='Nightmare')
#ed_user = Phase(name='Thrilling Escape and Return')

#5 Comedy
#ed_user = Phase(name='Establish the Status Quo')
#ed_user = Phase(name='Confusion and Isolation')
#ed_user = Phase(name='Raise the Stakes')
#ed_user = Phase(name='Problems Solved')


#6 Tragedy
#ed_user = Phase(name='The hero is tempted by something forbidden')
#ed_user = Phase(name='The hero commits to pursuing his dream, and it seems to be working')
#ed_user = Phase(name='The hero experiences a setback')
#ed_user = Phase(name='Everything spirals out of control')
#ed_user = Phase(name='The bad decisions have terrible consequences')


#7 Rebirth
#ed_user = Phase(name='A character falls under the spell of darkness')
#ed_user = Phase(name='The characters new status quo seems to be going well')
#ed_user = Phase(name='The threat returns or strengthens, and the charcter is stuck in a seemingly inescapable state of agony')
#ed_user = Phase(name='The agony continues, with no end in sight')
#ed_user = Phase(name='There is a final act of redemption')

