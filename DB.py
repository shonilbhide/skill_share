import os
from pymongo.mongo_client import MongoClient
import bson
from flask import current_app, g
from werkzeug.local import LocalProxy


def get_db():
    """
    Configuration method to return db instance
    """
    print("its here")
    db = getattr(g, "_database", None)
    if db is None:
      # Provide the mongodb atlas url to connect python to mongodb using pymongo
      CONNECTION_STRING = os.environ.get("DATABASE_URL", "mongodb+srv://skillswapapp:J4LGbdAHGX8uIPLu@cluster0.umwu3bv.mongodb.net/?retryWrites=true&w=majority")
      # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
      client = MongoClient(CONNECTION_STRING)
      # Create the database for our example (we will use the same database throughout the tutorial
      db = client['skillshare']
    return db


# Use LocalProxy to read the global db instance with just `db`
# db = LocalProxy(get_db)
