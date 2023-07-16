from db import db

class User(db.Model):
    __tablename__ = 'users'
    id:int = db.Column(db.Integer, primary_key=True)
    username:str = db.Column(db.String(50), unique=True, nullable=False)
    email:str = db.Column(db.String(80))

    def __init__(self,username, email, id=None):
        self.username = username
        self.email = email
        self.id = id

