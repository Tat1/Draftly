import sqlalchemy
from sqlalchemy import create_engine

#In memory Database
###engine = create_engine('sqlite:///:memory:', echo=True)

engine = create_engine('sqlite:///my-database.db', echo=True)

# Persistant file-based databse:
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class Plotline(Base) :
    __tablename__ = 'Plotline'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return "<Plotline(name='%s')>" % (self.name)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

ed_user = Plotline(name='Rebirth')
session.add(ed_user)
session.commit()

ed_user = Plotline(name='Comedy')
session.add(ed_user)
session.commit()

ed_user = Plotline(name='Voyage and Return')
session.add(ed_user)
session.commit()

ed_user = Plotline(name='The Quest')
session.add(ed_user)
session.commit()

ed_user = Plotline(name='Tragedy')
session.add(ed_user)
session.commit()

ed_user = Plotline(name='Overcoming the Monster')
session.add(ed_user)
session.commit()


class Role(Base) :
    __tablename__ = 'Role'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return "<Role(name='%s')>" % (self.name)
    
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

ed_user = Role(name='Antihero')
session.add(ed_user)
session.commit()

ed_user = Role(name='Confidant')
session.add(ed_user)
session.commit()

ed_user = Role(name='Love Interest')
session.add(ed_user)
session.commit()

ed_user = Role(name='Tertiary Character')
session.add(ed_user)
session.commit()

ed_user = Role(name='Deuteragonist')
session.add(ed_user)
session.commit()

ed_user = Role(name='Foil')
session.add(ed_user)
session.commit()

ed_user = Role(name='Quest Giver')
session.add(ed_user)
session.commit()

ed_user = Role(name='Antagonist')
session.add(ed_user)
session.commit()

ed_user = Role(name='Protagonist')
session.add(ed_user)
session.commit()


