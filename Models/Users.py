from mongoengine import Document, StringField, ListField, ReferenceField, EmbeddedDocument, EmbeddedDocumentField, IntField

class Skill(EmbeddedDocument):
    description = StringField(required=True)
    title = StringField(required=True)

class WantToLearn(EmbeddedDocument):
    description = StringField(required=True)
    title = StringField(required=True)

class WantToTeach(EmbeddedDocument):
    description = StringField(required=True)
    title = StringField(required=True)
    matched_users = ListField(ReferenceField('User'))

class ConnectedUser(EmbeddedDocument):
    user_id = ReferenceField('User')
    chat_id = StringField(required=True)

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

    meta = {'collection': 'users'}  # This specifies the collection name in MongoDB
