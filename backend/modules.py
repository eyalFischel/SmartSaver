from datetime import datetime
from pydantic import BaseModel

from mongoengine import Document, StringField, IntField

class User(Document):
    name = StringField(required=True)
    age = IntField(required=True)
    email = StringField()