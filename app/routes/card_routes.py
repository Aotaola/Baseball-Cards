from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://baseball_cards.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# CARDS ROUTES

@app.route('/cards')

@app.route('cards/id')

@app.route('create_card', methods='POST')

@app.route('add_card', methods = 'PATCH')

@app.route('delete_card', methods='DELETE')