from mongoengine import Document, StringField, ListField, ReferenceField, EmbeddedDocument, EmbeddedDocumentField, BooleanField, IntField
class MatchedUsers(EmbeddedDocument):
    user = ReferenceField('User')
    accepted_status = BooleanField()
    requested_status = BooleanField()

class Request(Document):
    # id = IntField()
    user = ReferenceField('User')
    vec = StringField()
    title = StringField(required=True)
    description = StringField(required=True)
    satisfied = BooleanField()
    matched_users = ListField(EmbeddedDocumentField(MatchedUsers))

    meta = {'collection': 'requests'}  # This specifies the collection name in MongoDB
