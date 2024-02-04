from flask import Blueprint, request, jsonify, json
from Models.Users import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

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
        data['password'] = generate_password_hash(data['password'])  # Hash the password
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
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid email or password'}), 401

    # Generate JWT token for authentication
    access_token = create_access_token(identity=str(user.id))
    return jsonify({'message': 'Login successful', 'access_token': access_token}), 200

# Protected route example using JWT token
@user_blueprint.route('/users/protected', methods=['GET'])
@jwt_required()
def protected_route():
    current_user_id = get_jwt_identity()  # Get current user ID from JWT token
    user = User.objects.get(email=current_user_id)
    return jsonify({'message': 'This is a protected route', 'user': user}), 200
