from mongoengine import Document, StringField, ListField, ReferenceField, EmbeddedDocument, EmbeddedDocumentField, BooleanField

class MatchedUsers(EmbeddedDocument):
    user = ReferenceField('User')
    req_id = ReferenceField('Request')
    accpeted_status = BooleanField()

class Request(Document):
    user = ReferenceField('User')
    vec = StringField()
    title = StringField(required=True)
    description = StringField(required=True)
    satisfied = BooleanField()
    matched_users = ListField(EmbeddedDocumentField(MatchedUsers))

    meta = {'collection': 'requests'}  # This specifies the collection name in MongoDB
