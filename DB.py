import os
from pymongo.mongo_client import MongoClient
from mongoengine import connect
import bson
from flask import current_app, g
from werkzeug.local import LocalProxy


def get_db():
    """
    Configuration method to return db instance
    """
    CONNECTION_STRING = os.environ.get("DATABASE_URL", "mongodb+srv://skillswapapp:J4LGbdAHGX8uIPLu@cluster0.umwu3bv.mongodb.net/?retryWrites=true&w=majority")

    connect('skillshare',host = CONNECTION_STRING)

