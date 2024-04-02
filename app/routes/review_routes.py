from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://baseball_cards.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# REVIEWS

@app.routes('reviews')

@app.routes('reviews/id')

@app.routes('create_review', methods='POST')

@app.routes('reviews_update', methods='PATCH')

@app.routes('delete_review', methods='DELETE')

