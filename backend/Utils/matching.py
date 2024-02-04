from Models.Users import User
from Models.Requests import Request,MatchedUsers
from Utils.TextUtils import *

def match(req_user_id, req_id, description):
    fields_to_select = ['id', 'want_to_teach']
    users = User.objects().only(*fields_to_select)

    result = []

    for user in users:
        if user.want_to_teach:
            for teach in user.want_to_teach:
                print(user.id)
                id, vec = user.id, teach.vec
                if vec:
                    result.append({
                        'user_id': str(id),
                        'description': vec
                    })

    model_path = './models/model.pkl'  # Specify the desired path to save the model

    embeddings = get_embeddings(description, load_model(model_path))

    incoming_data = {
        'req_user_id': req_user_id,
        'description': embeddings
    }
    top_matches = get_matches(incoming_data,result)

    req = Request.objects(id = req_id).first()
    user_ids = [top_match['user_id'] for top_match in top_matches]
    print(user_ids)
    i = 0
    temp_arr = []
    for user_id in user_ids:
        user = User.objects(id=user_id).first()
        matched_user = MatchedUsers(
            user=user,  # Provide a reference to the User object
            accepted_status=True,  # Provide a boolean value for accepted_status
            requested_status=False  # Provide a boolean value for requested_status
        )
        temp_arr.append(matched_user)
        i += 1

    print(temp_arr)

    req.matched_users = temp_arr

    req.save()
