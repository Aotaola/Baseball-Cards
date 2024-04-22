from flask import Blueprint, request, jsonify, redirect, url_for, session
from app.utils.database import db
#bcrypt
from app.models.review import Review 

review_bp = Blueprint('review_bp', __name__) 

# REVIEWS

@review_bp.route('/all_reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([{'id': review.id, 'body': review.review_body, 'card_id': review.review_card_id} for review in reviews])

@review_bp.route('/all_reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.get_or_404(review_id)
    return jsonify({'id': review.id, 'body': review.review_body, 'card_id': review.review_card_id})

@review_bp.route('/create_review', methods=['POST'])
def create_review():
    data = request.json
    new_review = Review(
        review_body=data['body'],
        review_card_id=data['card_id'],
        user_id=data['user_id']  
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'id': new_review.id, 'body': new_review.review_body, 'card_id': new_review.review_card_id, 'user_id': new_review.review_user_id}), 201

@review_bp.route('/edit_review/<int:review_id>', methods=['PATCH'])
def edit_review(review_id):
    review = Review.query.get_or_404(review_id)
    data = request.json
    review.review_body = data.get('body', review.review_body)
    db.session.commit()
    return jsonify({'id': review.id, 'body': review.review_body, 'card_id': review.review_card_id, 'user_id': review.user_id})

@review_bp.route('/delete_review/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'review deleted'}), 204

