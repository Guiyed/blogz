from app import db
from datetime import datetime

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))
    pub_date = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    
    def __init__(self, owner, title, body, pub_date=None):
        self.owner = owner
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.deleted = False
        

    def __repr__(self):
        return '<Blog %r>' % self.title

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    password = db.Column(db.String(32))
    email = db.Column(db.String(120),unique=True)
    blogs = db.relationship('Blog', backref='owner') 


    def __init__(self, username, password, email=None):
        self.username = username
        self.password = password
        if email is None:
            email = ''
        self.email = email


    def __repr__(self):
        return '<User %r>' % self.username
