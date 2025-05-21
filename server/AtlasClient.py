from pymongo import MongoClient
import os
from dotenv import load_dotenv

class AtlasClient:
    def __init__(self, dbname):
        load_dotenv()
        self.uri = os.getenv("MONGO_URI")
        self.mongodb_client = MongoClient(self.uri)
        self.database = self.mongodb_client[dbname]

    def ping(self):
        self.mongodb_client.admin.command('ping')

    def get_collection(self, collection_name):
        collection = self.database[collection_name]
        return collection

    def find(self, collection_name, filter={}, limit=0):
        collection = self.database[collection_name]
        items = list(collection.find(filter=filter, limit=limit))
        return items

    def get_user(self, email, password_hash):
        collection = self.database["users"]
        user = collection.find_one({"info.email": email, "info.password_hash": password_hash})
        if user is None:
            return {}
        del user["_id"]
        return user