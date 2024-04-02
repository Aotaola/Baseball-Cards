from flask import Flask
from utils.database import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baseball_cards.db'

db.init_app(app)


# Import models
from app.models.user import User
from app.models.collection import Collection
from app.models.card import Card
from app.models.review import Review

# Create database tables
with app.app_context():
    db.create_all()

# import blueprints
from app.routes.user_routes import user_bp
from app.routes.collection_routes import collection_bp
from app.routes.card_routes import card_bp
from app.routes.review_routes import review_bp

#register blueprints
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(collection_bp, url_prefix='/collections')
app.register_blueprint(card_bp, url_prefix='/cards')
app.register_blueprint(review_bp, url_prefix='/reviews')
