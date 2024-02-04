from flask import Blueprint, request, jsonify, json
from Models.Users import User

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
