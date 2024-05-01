from flask import Blueprint, request, jsonify, session
from app.utils.database import db
from app.extensions import bcrypt
from app.models.user import User
from flask_cors import CORS 

user_bp = Blueprint('user_bp', __name__)
CORS(user_bp)

@user_bp.route('/all_users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email, 'password': user.password_hash, 'collections': user.collections} for user in users])


@user_bp.route('/user/<int:user_id>', methods=['GET'])
def profile(user_id):
    user = User.query.filter_by(id=user_id).first()
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 200

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password_hash, data['password']):
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

#CREATE
@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    new_user = User(
        username=data['username'],
        email=data['email'],
        tokens= 100
    )
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id, 'username': new_user.username, 'email': new_user.email}), 201


@user_bp.route('/logout')
def logout():
    session.pop('session', None)
    return jsonify({'message': 'Logged out successfully'})

#PATCH
@user_bp.route('/update_user/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.bio = data.get('bio', user.bio)
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

#DELETE
@user_bp.route('/delete_user/<int:user_id>', methods=['DELETE'])

def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 204
