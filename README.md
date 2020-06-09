# Draftly

### Interactive Storytelling

My project currently called Draft is about providing a product or service which will be an Interactive Website that encourages gradual improvement for creative writing and freestyle. This in hope will inspire creativity and be an alternative interactive learning process that can be used. This pertains to writers or having an interest in writing.

---
### How to run [NEW]
Opted to build in Flask than Database method

In Terminal

Go to the Draft Interactive Directory

```
cd  /DraftInteractive
```

Things you need to install include

Install Homebrew
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Install either Pipenv
```
$ brew install pipenv
```

or Virtualenv
```
pip install virtualenv 
```
Install Python
```
$ brew install python

$ python3

# Do I have a Python 3 installed?
$ python --version
Python 3.7.1 # Success!
```

Install Flask
```
$ python3 -m venv venv

or

$ python2 -m virtualenv venv

source venv/bin/activate 

$ pip install Flask

```


Run the virtual environment

[Old]
```
export FLASK_APP=app  

flask run

http://localhost:5000/
```

[New]
```
FLASK_DEBUG=1 python app.py

http://localhost:5000/
```

For Mobile view
```
Your IP address:5000/
```
---
### Appearance Currently

* Home Page
![screen grab](https://github.com/Tat1/DraftInteractive/blob/master/screenshots/StartupV1.png)

* Load Story Page
![screen grab](https://github.com/Tat1/DraftInteractive/blob/master/screenshots/LoadstoryV1.png)

* New Story Page
![screen grab](https://github.com/Tat1/DraftInteractive/blob/master/screenshots/NewstoryV1.png)

* Character Creation Page
![screen grab](https://github.com/Tat1/DraftInteractive/blob/master/screenshots/CharactercreateV1.png)

* Story Paragraph Page
![screen grab](https://github.com/Tat1/DraftInteractive/blob/master/screenshots/StoryparaV1.png)

---
### Current Sitemap

![screen grab](https://github.com/Tat1/DraftInteractive/blob/master/screenshots/NewSiteMap2.jpg)

---

### Whats on Each Page

#### startup Page : http://localhost:5000/
Template: startup.html

Method: GET

* Button -> newstory.html -> (POST)
* Button -> loadstory.html -> (POST)

NOTE: 
* Contains Button to link to New Story Page
* Contains Button to link to Load Story Page


#### newstory Page : http://localhost:5000/newstory
Template: newstory.html

Method: POST

##### INCOMING FIELDS

* (none)

##### PAGE FORM

* Form Action -> charactercreation

  1)StorynameFormControlInput (Story Name)
  
  2)PlotlineControlSelect (Story Plotline)
  
* Button -> charactercreation -> (POST)

NOTE: 
* Contains Story Name
* Conatins Story Plotlines
* Story Plotlines (Dict. storyPlotlineToPhase) have Phases (Append. phasesForStory)
* Contains Button to link to the Character creation Page

#### charactercreation Page : http://localhost:5000/charactercreation
Template : charactercreation.html

Method : POST

##### INCOMING FIELDS (to the handler)

* First time into the page/handler from newstory:

- Story name
- Story plotline

* Subsequent times into the page/handler from itself! (charactercreation)

- Character Name
- Character Role
- Character Archetypes

##### PAGE FORM

* Form Action -> storyparagraphs
  
  1)CharacterFormControl (Character Name)
  
  2)RoleControlSelect (Character Role)
  
  3)ArchetypeControlSelect (Character Archetype)
  
* Button -> Create Character -> (VALUE)
* Button -> storyparagraphs -> (POST)
* List of Characters (Append. theCharacters)

  1)Name
  
  2)Role
  
  3)Arche 

NOTE:
* Contains Character Name
* Contains Character Role
* Contains Character Archetype
* Contains List of Character table with Name, Role and Archetype of all characters created
* Contains Button to create the character
* Contains Button to link to the Story Paragraph Page

#### storyparagraphs Page : http://localhost:5000/storyparagraphs
Template : storyparagraphs.html

Method : POST

* Badge -> StorynameFormControlInput (Story Name)
* Badge -> PlotlineControlSelect (Story Plotline)
* Badge -> List of Characters (Append. theCharacters)
* Phases (Append. phasesForStory) from (Dict. storyPlotlineToPhase)

  1)Phase Label
  
  2)paragraphsFormControlTextarea (Story Paragraph Text Area)
  
* Button -> Saves Fixed Story Paragraph, Moves to Next Story Phase -> (VALUE)

NOTE:
* Contains Story Name Label
* Contains Story Plotline Label
* Contains List of Character Table Label
* Conatins Phases and Paragraphs
* Contains Button for making the paragraphs fixed and moving to the next Story Phase

#### loadstory Page : http://localhost:5000/loadstory
Template : loadstory.html

Method : POST

NOTE:
* Future Development or Update for Selecting Multiple Story Works

---
# Database Aspect that I ended up not using

## Bare Bones of How it used to look like [OLD]

file:///Users/tatidisu/Documents/GitHub/DraftInteractive/app/templates/index.html

![screen grab](https://github.com/Tat1/DraftInteractive/blob/master/screenshots/Index%20Bare%20Draft.png)


# Concept Sketches

![screen grab](https://github.com/Tat1/DraftInteractive/blob/master/screenshots/Nav%20ver1.jpg)

# Database Sketch

![screen grab](https://github.com/Tat1/DraftInteractive/blob/master/screenshots/linkage.jpg)


---

### How to get it working

Using Pewee

https://github.com/coleifer/peewee

http://docs.peewee-orm.com/en/latest/peewee/installation.html


* Database with all the Databases 

```
source venv/bin/activate

python app/database/plotline.py

sqlite_web my-database.db 
```

![screen grab](https://github.com/Tat1/DraftInteractive/blob/master/screenshots/Database%20with%20Tables.png)


* Database with the foreign linkage

```
source venv/bin/activate

python app/database/tester.py

sqlite_web database.db
```
![screen grab](https://github.com/Tat1/DraftInteractive/blob/master/screenshots/Database%20with%20Linkage%20.png)


---

### Lists of Tables

There are 8 Tables, in which 5 are fixed entire applications and 3 are dynamic created by the user.

* Table of Story (Dynamic)

* Table of Character (Dynamic)

* Table of Paragraph (Dynamic)

* Table of Plotline (Fixed)

* Table of Roles (Fixed)

* Table of Archetype (Fixed)

* Table of Phase (Fixed)

* Table of Linkage (Fixed)

---

### Story (Dynamic)

This is populated by the user.
Name of  Story
New Story Created.
In a created Story, it contains the Paragraphs created by the user through forms, the Characters created by the user through forms and the plot lines chosen by the user which is fixed.

### Character (Dynamic)

Contains Name generated by User
Can choose Role (FIXED)
Paragraph contains characters
In the phases or mini subplots assigned to different character archetypes
Saved under one Story

### Paragraph (Dynamic)

Text Based
Contains Paragraphs the user creates

### Plotlines(Fixed)
Has 7 Basic Story Archetypes by Christopher Booker
It is fixed so select based

### Role (Fixed)
Has 7 Abstract Character Functions by Vladimir Propp
Roles are fixed 
List of all the character roles 
Select Based 
What role needs to be displayed in plot line and phase

### Archetype (FIXED)
Has 12 Jungian Archetypes by Carl Jung
Archetypes are fixed
List of all the archtype roles
select based
Under character role

### Phase (Fixed)
Has 7 Basic Story Archetypes by Christopher Booker and Story Empire Blog by Staci Troilo
Contains 34 subplots 
Depending on the plot line chosen associated subplots will be used
Characters created (roles) interact with subplots (1 character for 1 subplot) Dif Perspective
Interacts with the Prose the user writes through their paragraphs

### Linkage (Fixed)
3 Tables Plot, phase and role

---

### Rundown on how it will be connected

Schema Design for Interactive Storytelling

Simple SQL schema 
Tables with Primary keys and foreign keys 
No complicated linkage part from 1 Table that has 3 keys(Phase, Role, Plotline)

Schema divides into data that is completely Fixed (entire application) and Dynamic (created by the user). There are 4 completely fixed and 3 dynamic.

Table of Plotlines (7)
Potenital plots and templates 
Completely fixed user is required to pick a plot line 

Character of a story
There is a role for the character
the roles are completely fixed

As the story is written it goes through a set of phases and these phases are completely fixed

Dynamic in the schema 
You have stories
Create story with a name
The stories have to pick from a plot line 
Many to one relationships between story and plotline

Plotline has an ID the story has a foreign key linkage into the Plotline
As stories are built up there will be one plot line per story, potentially several stories could be on the same plot line(made by same user or made by someone different)

Stories have characters
Stories can have more than one character 
Every character has a preset role
Foreign key character that goes to primary key in role
(Potentially more than one character with a single role)
More than one hero and more than one villain, and might have no character for a particular role

Linkage from character to story which is many to one relationship
Story can have 1 or more characters 
Many to one linkage from character to role because every character has a role and the roles are preset 

Having set that up the user then gets to start writing paragraphs of text, 
got a table called prose where each entry in the table is a block of text
Every text paragraph is written form the point of view of a character  in a certain role

And the narrative voice switches between characters or between roles as the story progress
Linkage needed
If we link from each block/ entry of prose into the character  whose voice is speaking it that is many to one because the character may actually drop into the story more than once and have  more than one block of text 
from character we know we can get to the role of the character and we can get to the story and we can get to the plotline

These block of prose each associated with a phase of the story and again the phases are completely fixed and you work through phases as the stories get written 
The phases vary according to plot line, different plot line have to have different phases and each phase is associated with a role so the first phase is a certain role like hero, second could be villain, third could be something else.
So when I say a Line of text is written from the point of view of a character it has has to be a character of the correct role for the story according to the phase of the story 

Potentially when you are writing from a certain block of text you know what role it has to be 
Written in, which voice, because we know which phase of the story we are in because we are progressing through the phase if there is one character who has that role then you are telling the story from that characters point of view, if there is more than one character it could be a choice given to the user, right you are now in phase three you want  to write from the role of the villain and you have two villains so you need to  pick which one you want to write from 

Then the remaining bit of the Schema which we haven’t talked about is
How we link plot lines roles and phases
Given a plot line, that tells us what phases we go through and then for every phase we have a role for the character whose voice we are going to use.
We have a table here which is a table of 3 , foreign keys for plot, phase and role.

Given the plot line you can filter that table down, so that gives you phases and roles, as you work through the phases  that gives you the role you need to pick out for that phases and plot line in order to allow selection of the character and to have that block of text entered.
