from flask import Flask
from flask_bcrypt import Bcrypt
from utils.database import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://baseball_cards.db'
bcrypt = Bcrypt(app)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    body = db.Column(db.String, nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
