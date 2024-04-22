from flask import Flask
from flask_bcrypt import Bcrypt
from app.utils.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baseball_cards.db'
bcrypt = Bcrypt(app)


class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    collection_name = db.Column(db.String, nullable=False)
    collection_description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    collection_tokens = db.Column(db.Float)
    cards = db.relationship('Card', backref='collection', lazy='select')

    def value(self):
        total_value =  sum(card.value for card in self.cards)
        self.collection_tokens = total_value
        return total_value
    