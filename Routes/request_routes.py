from flask import Blueprint, request, jsonify, json
from Models.Requests import Request
from Models.Users import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

request_blueprint = Blueprint('request_blueprint', __name__)


@request_blueprint.get('/ping/requests')
def hello_requests():
    try:
        return "Pinged your deployment. You successfully connected to MongoDB!"
    except Exception as e:
        print(e)
        return "Error in Ping"

@request_blueprint.route('/requests', methods=['POST'])
@jwt_required()
def create_request():
    data = request.get_json()
    try:
        current_user_email = get_jwt_identity()
        user = User.objects(email = current_user_email).first()
        if user:
            req = Request(user=user,
                            title=data.get('title'),
                            description=data.get('description'),
                            matched_users = data.get('matched_users'),
                            satisfied = False)
            req.save()
            req_json = req.to_json()
            req_dict = json.loads(req_json)
            return jsonify(req_dict), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@request_blueprint.route('/users/requests', methods=['GET'])
@jwt_required()
def user_request_data():
    current_user_email = get_jwt_identity()
    user = User.objects(email = current_user_email).first()
    requests_of_user = None
    result = []
    if user:
        requests_of_user = Request.objects(user = user)
    if requests_of_user:
        for req in requests_of_user:
            if not req.satisfied:
                result.append({
                    "id":str(req.id),
                    "title": req.title,
                    "description": req.description
                })
    return result, 201

@request_blueprint.route('/requests/<id>', methods=['GET'])
@jwt_required()
def get_request_data(id):
    try:
        req = Request.objects(id=id).first()
        print(json.loads(req.to_json()).get("matched_users"))
        result = []
        for match in json.loads(req.to_json()).get("matched_users"):
            print(match)
            user = User.objects(id=match.get('user').get('$oid')).first()
            result.append({
                "email":user.email,
                "name":user.name,
                "description":user.description
            })
        return jsonify(result), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@request_blueprint.route('/match_request/send', methods=['POST'])
@jwt_required
def send_match_request():
    try:
        data = request.get_json()
        # data.user_id, -> to add the requests_i_have
        # data.req_id -> request to be get from request Objects and add it to the user
        requestedUser = User.objects(email = data.user_id)
        request = Request.objects.get(id=data.req_id)
        requestedUser.requests_i_have.append(request)
        print(requestedUser)
        requestedUser.save()
        return jsonify({'message': "Requested Succesfully"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
