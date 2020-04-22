from peewee import *

db = SqliteDatabase('database.db')


class Story(Model):
    name = 'storys'

    class Meta:
        database = db 

class Plotline(Model):
    child = ForeignKeyField(Story, backref='plotlines')
    name = 'plotlines'
    
    #ed_user = Plotline.create(name='Overcoming the Monster')
    #ed_user.save()

    class Meta:
        database = db 
        
db.connect()

db.create_tables([Story, Plotline])
        
