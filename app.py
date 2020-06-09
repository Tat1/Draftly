from flask import Flask, render_template, request

app = Flask(__name__)

# Keep a hold of the stort name and plot type!!!!

storyName = None
storyPlotline = None
PlotlineControlSelect = None

thePhases = []
theCharacters = []
phasesForStory = None


# STORIES = ['OvercomingTheMonster', 'RagsToRiches', 'Quest', 'VoyageAndReturn', 'Comedy', 'Tradegy','Rebirth' ]
storyPlotlineToPhase = {
    'Overcoming The Monster' : ['Anticipation', 'Dream', 'Frustration', 'Nightmare', 'Miraculous Escape'],
    'Rags To Riches' : ['Initial Wretchedness then Call to Action', 'Getting out into the World', 'Central Crisis', 'Independence and Ordeal', 'Fulfillment'],
    'Quest' : ['The Call', 'The Journey', 'Arrival and Frustration', 'Final Ordeal', 'The Goal'],
    'Voyage and Return' : ['Anticipation Stage and Fall into Another World','Initial Fascination or Dream Stage','Frustration','Nightmare','Thrilling Escape and Return' ],
    'Comedy' : ['Establish the Status Quo','Confusion and Isolation','Raise the Stakes','Problems Solved'],
    'Tragedy' : ['Hero is Tempted', 'Pursue Dream','Setback','Spiralling out of control','Decision and Consequence' ],
    'Rebirth' : ['Spell of Darkness', 'New Status Quo', 'Threat and Agony', 'Agony Continues', 'Redemption']
    }

#Using Jinja
@app.route('/',  methods = ['GET'])
def startup():
    return render_template('index.html')

@app.route('/newstory', methods = ['POST'])
def newstory():

    return render_template('newstory.html')

@app.route('/storyparagraphs', methods = ['POST'])
def storyparagraphs():
    global phasesForStory, storyName, storyPlotline, PlotlineControlSelect
    
    if 'paragraphsFormControlTextarea1' in request.form:
            phaseName = storyPlotlineToPhase[storyPlotline][len(thePhases)]
            textName = request.form.get('paragraphsFormControlTextarea1')
            #paragraphsFormControlTextarea1
            
            thePhases.append({'phase' : phaseName,
                              'text' : textName})
    else:
        print('No form Data')
                
        

    return render_template('storyparagraphs.html', storyName=storyName, storyPlotline=storyPlotline, characters=theCharacters, phases=thePhases)
#phasesForStory=phasesForStory


@app.route('/loadstory', methods = ['POST'])
def loadstory():
    return render_template('loadstory.html')

@app.route('/charactercreation', methods = ['POST'])
def charactercreation():
    global phasesForStory, storyName, storyPlotline, PlotlineControlSelect

    # Comes in on first access:
    if 'PlotlineControlSelect' in request.form:
        storyName = request.form.get('StorynameFormControlInput')
        storyPlotline = request.form.get('PlotlineControlSelect')
        phasesForStory = storyPlotlineToPhase[storyPlotline]
        # And continue
    else:
        charName = request.form.get('CharacterFormControl')
        roleName = request.form.get('RoleControlSelect')
        archetypeName = request.form.get('ArchetypeControlSelect')

        theCharacters.append({'name' : charName,
                              'role' : roleName,
                              'arche' : archetypeName})

    # Store as a Python dictionary:

    return render_template('charactercreation.html', storyName=storyName, storyPlotline=storyPlotline, characters=theCharacters, phasesForStory=phasesForStory)

#app.run(host='0.0.0.0')
const PORT = process.env.PORT || '8080'

app.set("port", PORT);
#log.Fatal(http.ListenAndServe(":" + os.Getenv("PORT"), router))



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
