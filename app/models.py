from app.database import db

profiles_collection = db["profiles"]

def create_profile(data: dict):
    profiles_collection.insert_one(data)

def get_profile_by_user_id(user_id: str):
    return profiles_collection.find_one({"user_id": user_id}, {"_id": 0})
