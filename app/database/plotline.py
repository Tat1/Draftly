import sqlalchemy
from sqlalchemy import create_engine

#In memory Database
###engine = create_engine('sqlite:///:memory:', echo=True)

engine = create_engine('sqlite:///my-database.db', echo=True)

# Persistant file-based databse:
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base) :
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return "<User(name='%s')>" % (self.name)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

ed_user = User(name='Rebirth')
session.add(ed_user)
session.commit()

ed_user = User(name='Comedy')
session.add(ed_user)
session.commit()