from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://baseball_cards.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String(60))
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    bio = db.Column(db.Text)
    tokens = db.Column(db.Float)

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    collection_name = db.Column(db.String, nullable=False)
    collection_description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeingKey('user.id'))
    collection_tokens = db.Column(db.Float)
    
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    popularity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    player = db.Column(db.String, nullable=False)
    image = db.Column(db.BLOB)#blob stands for binary large object
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id') )

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    body = db.Column(db.String, nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@app.route('/')

def hello():
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)