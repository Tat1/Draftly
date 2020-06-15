
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# Persistant file-based databse:
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String

from peewee import *

#In memory Database
###engine = create_engine('sqlite:///:memory:', echo=True)

engine = create_engine('sqlite:///my-database.db', echo=True)


Base = declarative_base()

#Many to one between story and plotline, stories have foreign key linksge , primary key to plotline
# Story (DYNAMIC)
class Story(Base) :
    __tablename__ = 'story'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    plot_id = Column(Integer, ForeignKey('plotline.id'))
    
    plot = relationship("Plotline", foreign_keys=[plot_id])

    def __repr__(self):
        return "<Story(name='%s')>" % (self.name)

    
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()


#Character has foreign key that goes to role, linkage from character to story many to one, many to one linkage from character to role
# Character (DYNAMIC)
class Character(Base) :
    __tablename__ = 'character'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return "<Character(name='%s')>" % (self.name)
    
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()


#linkage from paragraph into charcater many to one, character-> role-> story-> plotline
# Paragraph (DYNAMIC)
class Paragraph(Base) :
    __tablename__ = 'paragraph'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return "<Paragraph(name='%s')>" % (self.name)
    
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()


# Plotline (FIXED)
#7 Basic Story Archetypes by Christopher Booker
class Plotline(Base) :
    __tablename__ = 'plotline'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Plotline(name='%s')>" % (self.name)

Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

ed_user = Plotline(name='Overcoming the Monster')
session.add(ed_user)
session.commit()

ed_user = Plotline(name='Rags to Riches')
session.add(ed_user)
session.commit()

ed_user = Plotline(name='The Quest')
session.add(ed_user)
session.commit()

ed_user = Plotline(name='Voyage and Return')
session.add(ed_user)
session.commit()

ed_user = Plotline(name='Comedy')
session.add(ed_user)
session.commit()

ed_user = Plotline(name='Tragedy')
session.add(ed_user)
session.commit()

ed_user = Plotline(name='Rebirth')
session.add(ed_user)
session.commit()


# Role (FIXED)
#7 Abstract Character Functions by Vladimir Propp
class Role(Base) :
    __tablename__ = 'role'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return "<Role(name='%s')>" % (self.name)
    
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

ed_user = Role(name='The Villain')
session.add(ed_user)
session.commit()

ed_user = Role(name='The Dispatcher')
session.add(ed_user)
session.commit()

ed_user = Role(name='The Helper')
session.add(ed_user)
session.commit()

ed_user = Role(name='The Love Interest')
session.add(ed_user)
session.commit()

ed_user = Role(name='The Donor')
session.add(ed_user)
session.commit()

ed_user = Role(name='The Hero')
session.add(ed_user)
session.commit()

ed_user = Role(name='The False Hero')
session.add(ed_user)
session.commit()


# Archetype (FIXED)
#12 Jungian Archetypes by Carl Jung
class Archetype(Base) :
    __tablename__ = 'archetype'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return "<Archetype(name='%s')>" % (self.name)
    
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

#Ego Types
ed_user = Archetype(name='Innocent')
session.add(ed_user)
session.commit()

ed_user = Archetype(name='Orphan')
session.add(ed_user)
session.commit()

ed_user = Archetype(name='Hero')
session.add(ed_user)
session.commit()

ed_user = Archetype(name='Caregiver')
session.add(ed_user)
session.commit()

#Soul Types
ed_user = Archetype(name='Explorer')
session.add(ed_user)
session.commit()

ed_user = Archetype(name='Rebel')
session.add(ed_user)
session.commit()

ed_user = Archetype(name='Lover')
session.add(ed_user)
session.commit()

ed_user = Archetype(name='Creator')
session.add(ed_user)
session.commit()

#Self Types
ed_user = Archetype(name='Jester')
session.add(ed_user)
session.commit()

ed_user = Archetype(name='Sage')
session.add(ed_user)
session.commit()

ed_user = Archetype(name='Magician')
session.add(ed_user)
session.commit()

ed_user = Archetype(name='Ruler')
session.add(ed_user)
session.commit()


# Phase (FIXED)
#7 Basic Story Archetypes by Christopher Booker
#Story Empire Blog by Staci Troilo
class Phase(Base) :
    __tablename__ = 'phase'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return "<Phase(name='%s')>" % (self.name)
    
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

#1 Overcoming The Monster
ed_user = Phase(name='Anticipation')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Dream')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Frustration')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Nightmare')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Miraculous Escape')
session.add(ed_user)
session.commit()

#2 Rags to Riches
ed_user = Phase(name='Initial Wretchedness then Call to Action')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Getting out into the World')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Central Crisis')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Independence and Ordeal')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Fulfillment')
session.add(ed_user)
session.commit()

#3 Quest
ed_user = Phase(name='The Call')
session.add(ed_user)
session.commit()

ed_user = Phase(name='The Journey')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Arrival and Frustration')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Final Ordeal')
session.add(ed_user)
session.commit()

ed_user = Phase(name='The Goal')
session.add(ed_user)
session.commit()

#4 Voyage and Return
ed_user = Phase(name='Anticipation Stage and Fall into Another World')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Initial Fascination or Dream Stage')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Frustration')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Nightmare')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Thrilling Escape and Return')
session.add(ed_user)
session.commit()

#5 Comedy
ed_user = Phase(name='Establish the Status Quo')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Confusion and Isolation')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Raise the Stakes')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Problems Solved')
session.add(ed_user)
session.commit()

#6 Tragedy
ed_user = Phase(name='The hero is tempted by something forbidden')
session.add(ed_user)
session.commit()

ed_user = Phase(name='The hero commits to pursuing his dream, and it seems to be working')
session.add(ed_user)
session.commit()

ed_user = Phase(name='The hero experiences a setback')
session.add(ed_user)
session.commit()

ed_user = Phase(name='Everything spirals out of control')
session.add(ed_user)
session.commit()

ed_user = Phase(name='The bad decisions have terrible consequences')
session.add(ed_user)
session.commit()

#7 Rebirth
ed_user = Phase(name='A character falls under the spell of darkness')
session.add(ed_user)
session.commit()

ed_user = Phase(name='The characters new status quo seems to be going well')
session.add(ed_user)
session.commit()

ed_user = Phase(name='The threat returns or strengthens, and the charcter is stuck in a seemingly inescapable state of agony')
session.add(ed_user)
session.commit()

ed_user = Phase(name='The agony continues, with no end in sight')
session.add(ed_user)
session.commit()

ed_user = Phase(name='There is a final act of redemption')
session.add(ed_user)
session.commit()


# Linkage (FIXED)
class Linkage(Base) :
    __tablename__ = 'linkage'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return "<Linkage(name='%s')>" % (self.name)
    
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

#link plotline roles and phases, given plotline tells phase and every phase has a role
#Table - 3 Foreign keys for plot, phase, role


