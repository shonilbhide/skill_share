# To install the lib
# python3 -m venv .venv
# source .venv/bin/activate
# python -m pip install "pymongo[srv]"


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://skillswapapp:J4LGbdAHGX8uIPLu@cluster0.umwu3bv.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
