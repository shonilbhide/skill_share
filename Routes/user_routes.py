from datetime import timedelta
from flask import Blueprint, request, jsonify, json
from Models.Users import User
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import bcrypt

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.get('/ping')
def hello():
    try:
        return "Pinged your deployment. You successfully connected to MongoDB!"
    except Exception as e:
        print(e)
        return "Error in Ping"

@user_blueprint.post('/users')
def add_user():
    try:
        user_data = request.json
        user = User(**user_data)
        user.save()
        user_json = user.to_json()
        user_dict = json.loads(user_json)
        return jsonify(user_dict), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Signup API with password hashing
@user_blueprint.route('/users/signup', methods=['POST'])
def signup():
    data = request.get_json()
    user = User.objects(email=data['email']).first()
    if not user:
        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        data['password'] = hashed_password.decode('utf-8')
        user = User(**data)
        user.save()
        # Generate JWT token for authentication
        access_token = create_access_token(identity=str(user.email))
        return jsonify({'message': 'User registered successfully', 'access_token': access_token}), 200
    else:
        return jsonify({'message': 'User is already Registered, please Login'}), 400

# Login API with JWT token generation
@user_blueprint.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.objects(email=email).first()
    print(user.email)
    if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return jsonify({'message': 'Invalid email or password'}), 401

    # Generate JWT token for authentication
    access_token = create_access_token(identity=str(user.email), expires_delta=timedelta(days=30))
    return jsonify({'message': 'Login successful', 'access_token': access_token}), 200


# Protected route example using JWT token
@user_blueprint.route('/user_profile', methods=['GET'])
@jwt_required()
def user_profile():
    current_user_email = get_jwt_identity()
    user_from_db = User.objects(email = current_user_email)
    print(user_from_db[0].want_to_teach)
    if user_from_db:
        result_obj = {
            "name": user_from_db[0].name,
            "email": user_from_db[0].email,
            "description": user_from_db[0].description,
            "skill_hours": user_from_db[0].skill_hours,
            "want_to_teach":[ req.to_json() for req in user_from_db[0].want_to_teach ],
        }
    return result_obj, 201
