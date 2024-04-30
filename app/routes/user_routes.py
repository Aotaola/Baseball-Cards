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
    content_type = request.content_type.split(';')[0].strip()
    if content_type not in ('application/json', 'multipart/form-data'):
        return jsonify({'error': 'Unsupported Content-Type'}), 400

    if content_type == 'application/json':
        data = request.json
    else:
        data = request.form.to_dict()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    required_fields = ['username', 'email', 'password']  # Adjust as needed
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({'error': f'Missing or empty field: {field}'}), 400

    new_user = User(
        username=data['username'],
        email=data['email'],
        bio=data.get('bio', ''),  # Use get() to handle optional fields
        tokens=100  # Default value for tokens, adjust as needed
    )
    new_user.set_password(data['password'])

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error'}), 500

    return jsonify({
        'message': 'User created successfully',
        'user': {
            'username': new_user.username,
            'email': new_user.email,
            'bio': new_user.bio,
            'tokens': new_user.tokens
        }
    }), 201  # 201 Created status code for successful creation


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
