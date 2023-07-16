from db import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer)

    def __init__(self, name:str, price:int=None, id:int=None):
        self.id = id
        self.name = name
        self.price = price
