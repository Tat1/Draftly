from flask import Flask, render_template, request

app = Flask(__name__)

theCharacters = []

# STORIES = ['OvercomingTheMonster', 'RagsToRiches', 'Quest', 'VoyageAndReturn', 'Comedy', 'Tradegy','Rebirth' ]
storyPlotlineToPhase = {
    'Overcoming_The_Monster' : ['Anticipation', 'Dream', 'Frustration', 'Nightmare', 'Miraculous_Escape'],
    'Rags_To_Riches' : ['Initial_Wretchedness_then_Call_to_Action', 'Getting_out_into_the_World', 'Central_Crisis', 'Independence_and_Ordeal', 'Fulfillment'],
    'Quest' : ['The Call', 'The Journey', 'Arrival_and_Frustration', 'Final_Ordeal', 'The Goal'],
    'Voyage_and_Return' : ['Anticipation_Stage_and_Fall_into_Another_World','Initial_Fascination_or_Dream_Stage','Frustration','Nightmare','Thrilling_Escape_and_Return' ],
    'Comedy' : ['Establish_the_Status_Quo','Confusion_and_Isolation','Raise_the_Stakes','Problems_Solved'],
    'Tragedy' : ['Hero_is_Tempted', 'Pursue_Dream','Setback','Spiralling_out_of_control','Decision_and_Consequence' ],
    'Rebirth' : ['Spell_of_Darkness', 'New_Status_Quo', 'Threat_and_Agony', 'Agony_Continues', 'Redemption'] 
    }

#Using Jinja
@app.route('/',  methods = ['GET'])
def startup():
    return render_template('startup.html')

@app.route('/newstory', methods = ['POST'])
def newstory():

    return render_template('newstory.html', characters=theCharacters)

@app.route('/storyparagraphs', methods = ['POST'])
def storyparagraphs():

    storyPlotline = request.form["PlotlineControlSelect"]
    
    phasesForStory = storyPlotlineToPhase[storyPlotline]

    
    return render_template('storyparagraphs.html', StorynameFormControlInput=request.form['StorynameFormControlInput'], PlotlineControlSelect=request.form['PlotlineControlSelect'], characters=theCharacters, phasesForStory=phasesForStory)


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

