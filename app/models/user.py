from flask import Flask
from flask_bcrypt import Bcrypt
from app.utils.database import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://baseball_cards.db'
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String(60))
    collections = db.relationship('Collection', backref='owner', lazy='True')


    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    bio = db.Column(db.Text)
    tokens = db.Column(db.Float)

    #token value

    def total_value(self):
        return sum(collection.value for collection in self.collection)
    
