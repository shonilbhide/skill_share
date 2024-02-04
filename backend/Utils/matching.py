from Models.Users import User
from TextUtils import *

def match(req_user_id, description):
    fields_to_select = ['id', 'description']
    users = User.objects().only(*fields_to_select)

    print(users)
    result = []
    for user in users:
        id, description = user.id, user.description
        result.append({
            'user_id': str(id),
            'description': description
        })
    
    print(result)

    incoming_data = {
        'req_user_id': req_user_id,
        'description': description
    }
    top_matches = get_matches(incoming_data,result)
    pass