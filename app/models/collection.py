from flask import Flask
from flask_bcrypt import Bcrypt
from utils.database import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://baseball_cards.db'
bcrypt = Bcrypt(app)

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    collection_name = db.Column(db.String, nullable=False)
    collection_description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeingKey('user.id'))
    collection_tokens = db.Column(db.Float)
    