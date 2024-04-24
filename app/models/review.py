from flask import Flask
from flask_bcrypt import Bcrypt
from app.utils.database import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:password@baseball-card-backend-db.c98ugqo62jg6.us-east-1.rds.amazonaws.com:3306/baseball_cards'
bcrypt = Bcrypt(app)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    body = db.Column(db.Text, nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
