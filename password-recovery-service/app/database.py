from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://recovery-db:27017/")
client = MongoClient(MONGO_URL)
db = client["password_recovery"]
