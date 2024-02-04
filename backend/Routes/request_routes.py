from flask import Blueprint, request, jsonify, json
from Models.Requests import Request
from Models.Users import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from Models.Users import RequestsIHave
from Utils.matching import match
import threading

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
        desc = data.get('description')
        if user:
            req = Request(user=user,
                            title=data.get('title'),
                            description=desc,
                            matched_users = data.get('matched_users'),
                            satisfied = False)
            req.save()
            req_json = req.to_json()
            req_dict = json.loads(req_json)
            print(desc)
            thread = threading.Thread(target=match, args= (user.id, str(desc),))
            thread.start()

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


@request_blueprint.route('/match_request/send/<id>/user/<user_email>', methods=['POST'])
@jwt_required()
def send_match_request(id, user_email):
    try:
        # current_user_email = get_jwt_identity()
        # print("Its here ", id, current_user_email)
        # data.user_id, -> to add the requests_i_have
        # data.req_id -> request to be get from request Objects and add it to the user
        requestedUser = User.objects(email = user_email).first()
        print("Its here req User ", requestedUser)
        req = Request.objects.get(id=id)
        print("Its here req ", req)
        reqIHave = RequestsIHave()
        reqIHave.req = req
        reqIHave.accepted_status = False
        requestedUser.requests_i_have.append(reqIHave)
        print(requestedUser)
        requestedUser.save()
        return jsonify({'message': "Requested Succesfully"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@request_blueprint.route('/request/accept/<id>', methods=['POST'])
@jwt_required()
def accepet_match_request(id):
    try:
        # Request -> satisfied = True
        # Request -> matched_users -> map user_id and make accepted_status = True
        # User -> Update Requests I Have and update accepted_status = True
        current_user_email = get_jwt_identity()
        acceptedUser = User.objects(email = current_user_email).first()
        req = Request.objects.get(id=id)
        temp = []
        for r in acceptedUser.requests_i_have:
            if r.req != req:
                temp.append(r)
        acceptedUser.requests_i_have = temp
        print(acceptedUser)
        acceptedUser.save()
        req.satisfied = True
        temp = []
        print("its ",req.matched_users)
        for r in req.matched_users:
            if r.user == acceptedUser:
                r.accepted_status = True
            temp.append(r)
        print("its here temp ", temp)
        req.matched_users = temp
        req.save()
        return jsonify({'message': "Requested Succesfully"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
