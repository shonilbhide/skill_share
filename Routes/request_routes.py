from flask import Blueprint, request, jsonify, json
from Models.Requests import Request
from Models.Users import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from Models.Users import RequestsIHave

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
            req = Request(
                user=user,
                title=data.get('title'),
                description=data.get('description'),
                satisfied = False
                )
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
    print("User email ", current_user_email)
    user = User.objects(email = current_user_email).first()
    print("User ", user.id)
    requests_of_user = Request.objects(user = user)
    print(requests_of_user)
    result = []
    if requests_of_user:
        for req in requests_of_user:
            if not req.satisfied:
                result.append({
                    "id":str(req._id),
                    "title": req.title,
                    "description": req.description
                })
    return result, 201

@request_blueprint.route('/requests/<id>', methods=['GET'])
@jwt_required()
def get_request_data(id):
    try:
        req = Request.objects.get(id=id).first()
        result = []
        for match in req.matched_users:
            result.append({
                "email":match.user.email,
                "name":match.user.name,
                "description":match.user.description
            })
        return result, 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@request_blueprint.route('/match_request/send/<id>', methods=['POST'])
@jwt_required()
def send_match_request(id):
    try:
        current_user_email = get_jwt_identity()
        print("Its here ", id, current_user_email)
        # data.user_id, -> to add the requests_i_have
        # data.req_id -> request to be get from request Objects and add it to the user
        requestedUser = User.objects(email = current_user_email).first()
        print("Its here req User ", requestedUser)
        req = Request.objects.get(id=id)
        print("Its here req ", req)
        reqIHave = RequestsIHave()
        reqIHave.req = req
        requestedUser.requests_i_have.append(reqIHave)
        print(requestedUser)
        requestedUser.save()
        return jsonify({'message': "Requested Succesfully"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@request_blueprint.route('/request/accept', methods=['POST'])
@jwt_required
def accepet_match_request():
    try:
        data = request.get_json()
        # Request -> satisfied = True
        # Request -> matched_users -> map user_id and make accepted_status = True
        # User -> Update Requests I Have and update accepted_status = True
        acceptedUser = User.objects(email = data.user_id).first()
        req = Request.objects.get(id=data.req_id).first()
        temp = []
        for r in acceptedUser.requests_i_have:
            if r.id != req._id:
                temp.append(r)
        acceptedUser.requests_i_have = temp
        print(acceptedUser)
        acceptedUser.save()
        req.satisfied = True
        temp = []
        for r in req.matched_users:
            if r.user == acceptedUser:
                r.accepted_status = True
            temp.append(r)

        req.matched_users = temp
        req.save()
        return jsonify({'message': "Requested Succesfully"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@request_blueprint.route('/request/user', methods=['POST'])
@jwt_required
def accepet_match_request():
    try:
        data = request.get_json()
        # Request -> satisfied = True
        # Request -> matched_users -> map user_id and make accepted_status = True
        # User -> Update Requests I Have and update accepted_status = True
        acceptedUser = User.objects(email = data.user_id).first()
        req = Request.objects.get(id=data.req_id).first()
        temp = []
        for r in acceptedUser.requests_i_have:
            if r.id != req._id:
                temp.append(r)
        acceptedUser.requests_i_have = temp
        print(acceptedUser)
        acceptedUser.save()
        req.satisfied = True
        temp = []
        for r in req.matched_users:
            if r.user == acceptedUser:
                r.accepted_status = True
            temp.append(r)

        req.matched_users = temp
        req.save()
        return jsonify({'message': "Requested Succesfully"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
