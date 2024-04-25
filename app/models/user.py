from flask import Flask
from flask_bcrypt import Bcrypt
from app.utils.database import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:password@baseball-card-backend-db.c98ugqo62jg6.us-east-1.rds.amazonaws.com:3306/baseball_cards'
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(60))
    image_url = db.Column(db.Text)
    collections = db.relationship('Collection', backref='owner', lazy='select')


    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    bio = db.Column(db.Text)
    tokens = db.Column(db.Float)

    #token value

    def total_value(self):
        collection_value = sum(collection.value for collection in self.collection)
        self.tokens += collection_value
        return self.tokens

    
