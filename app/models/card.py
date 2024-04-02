from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://baseball_cards.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    popularity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    player = db.Column(db.String, nullable=False)
    image = db.Column(db.BLOB)#blob stands for binary large object
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id') )
