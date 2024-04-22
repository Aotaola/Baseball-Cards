from flask import Blueprint, request, jsonify, session
from app.utils.database import db
from app.extensions import bcrypt
from app.models.user import User 

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/profile', methods=['GET'])
def profile(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user

@user_bp.route('/login', methods=['POST'])

def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password_hash, data['password']):
        return jsonify({'message': 'Login successful', 'user': {'username': user.username, 'email': user.email}})
    else:
        return jsonify({'message': 'Invalid username or password'}), 401


@user_bp.route('/signup', methods=['POST'])

def signup():
    data = request.json
    new_user = User(
        username=data['username'],
        email=data['email'],
        bio=data['bio'],
        tokens= 100
    )
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully', 'user': {'username': new_user.username, 'email': new_user.email, 'bio': new_user.bio, 'tokens': new_user.tokens}})


@user_bp.route('/logout')

def logout():
    session.pop('session', None)
    return jsonify({'message': 'Logged out successfully'})

@user_bp.route('/update_user/<int:user_id>', methods=['PATCH'])

def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.bio = data.get('bio', user.bio)
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})


@user_bp.route('/delete_user/<int:user_id>', methods=['DELETE'])

def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 204
