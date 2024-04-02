from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://baseball_cards.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

@app.route('/collections')

@app.route('/collections/id')

@app.route('/create_collection', methods='POST')

@app.route('/edit_collection', methods='PATCH')

@app.route('delete_collection', methods='DELETE')
