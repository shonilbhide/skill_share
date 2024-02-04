from mongoengine import Document, StringField, ListField, ReferenceField, EmbeddedDocument, EmbeddedDocumentField, IntField, BooleanField

class Skill(EmbeddedDocument):
    description = StringField(required=True)
    title = StringField(required=True)

class WantToLearn(EmbeddedDocument):
    description = StringField(required=True)
    title = StringField(required=True)

class WantToTeach(EmbeddedDocument):
    description = StringField(required=True)
    title = StringField(required=True)

    def to_json(self):
        return {
            'description': self.description,
            'title': self.title
        }

class ConnectedUser(EmbeddedDocument):
    user_id = ReferenceField('User')
    chat_id = StringField(required=True)

class RequestsIHave(EmbeddedDocument):
    req = ReferenceField('Request')
    accepted_status = BooleanField()

class User(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    phone = StringField(required=True)
    password = StringField(required=True)
    description = StringField()
    want_to_learn = ListField(EmbeddedDocumentField(WantToLearn))
    want_to_teach = ListField(EmbeddedDocumentField(WantToTeach))
    skill_hours = IntField()
    wallet_id = StringField()
    connected_users = ListField(EmbeddedDocumentField(ConnectedUser))
    requests_i_have = ListField(EmbeddedDocumentField(RequestsIHave))

    meta = {'collection': 'users'}  # This specifies the collection name in MongoDB
