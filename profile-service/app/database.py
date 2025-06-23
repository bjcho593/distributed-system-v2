from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://profile-db:27017/")
client = MongoClient(MONGO_URL)
db = client["user_profiles"]
