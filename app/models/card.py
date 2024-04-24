from flask import Flask
from app.extensions import Bcrypt
from app.utils.database import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baseball_cards.db'
bcrypt = Bcrypt(app)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    popularity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    player = db.Column(db.String, nullable=False)
    image = db.Column(db.TEXT)#image url
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id') )
    # gas_tax = db.Column(db.Float, default=0.05)

    # def __init__(self) -> None:
    #     super(Card, self).__init__(*args, **kwargs)
    #     self.apply_gas_tax()

    # def apply_gas_tax(self):
    #     tax_amount = self.value * self.gas_tax
    #     self.collection.value -= tax_amount
