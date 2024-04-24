from flask import Blueprint, request, jsonify
from app.utils.database import db
from app.models.card import Card 
from flask_cors import CORS

card_bp = Blueprint('card_bp', __name__)
CORS(card_bp)

# CARDS ROUTES
#GET
    #get all cards
@card_bp.route('/cards', methods=['GET'])
def get_cards():
    cards = Card.query.all()
    return jsonify([{'id': card.id, 'popularity': card.card_popularity, 'price': card.card_price, 'player': card.card_player, 'image': card.card_image, 'collection_id': card.card_collection_id} for card in cards])
    #get card by id
@card_bp.route('/cards/<int:card_id>', methods=['GET'])
def get_card(card_id):
    card = Card.query.get_or_404(card_id)
    return jsonify({'id': card.id, 'player': card.card_player, 'image': card.card_image, 'tokens': card.card_tokens})

#CREATE
@card_bp.route('/create_card', methods=['POST'])
def create_card():
    data = request.json
    new_card = Card(
        card_player=data['player'],
        card_image=data['image'],
        user_id=data['user_id']  # Assuming you have a user_id field to link the card to a user
    )
    db.session.add(new_card)
    db.session.commit()
    return jsonify({'id': new_card.id, 'popularity': new_card.card_popularity, 'price': new_card.card_price, 'player': new_card.card_player, 'image': new_card.card_image, 'collection_id': new_card.card_collection_id})
#PATCH
@card_bp.route('/edit_card/<int:card_id>', methods=['PATCH'])
def edit_card(card_id):
    card = Card.query.get_or_404(card_id)
    data = request.json
    card.popularity = data.get('popularity', card.card_popularity)
    card.price = data.get('price', card.card_price)
    card.card_player = data.get('player', card.card_player)
    card.card_image = data.get('image', card.card_image)
    card.collection_id = data.get('collection_id', card.collection_id)
    db.session.commit()
    return jsonify({'id': card.id, 'popularity': card.card_popularity, 'price': card.card_price, 'player': card.card_player, 'image': card.card_image, 'collection_id': card.card_collection_id})
#DELETE
@card_bp.route('/delete_card/<int:card_id>', methods=['DELETE'])
def delete_card(card_id):
    card = Card.query.get_or_404(card_id)
    db.session.delete(card)
    db.session.commit()
    return jsonify({'message': 'card deleted'}), 204