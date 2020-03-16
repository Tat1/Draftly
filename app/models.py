from app import db

class Plotline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Plotline = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Plotline {}>'.format(self.username)    
    
    
    