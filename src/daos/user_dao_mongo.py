"""
User DAO Mongo (Data Access Object for MongoDB)
Auteurs : Jean-Christophe Caron, 2025
"""

import os
from dotenv import load_dotenv
from pymongo import MongoClient
from models.user import User
from bson import ObjectId

class UserMongoDAO:
    def __init__(self):
        try:
            env_path = ".env"
            print(os.path.abspath(env_path))
            load_dotenv(dotenv_path=env_path)
            
            db_host = os.getenv("MONGODB_HOST")
            db_port = int(os.getenv("MONGODB_PORT", 27017))
            db_name = os.getenv("DB_NAME")
            db_user = os.getenv("DB_USERNAME")
            db_pass = os.getenv("DB_PASSWORD")
            
            if not all([db_host,db_port,db_user,db_pass,db_name]):
                raise RuntimeError("Variables d'environnement MongoDB manquantes")
            
            mongo_uri = f"mongodb://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}?authSource=admin"
            self.client = MongoClient(mongo_uri)
            self.db = self.client[db_name]
            self.collection = self.db["users"]

        except FileNotFoundError as e:
            print("Attention : Veuillez créer un fichier .env")
        except Exception as e:
            print("Erreur : " + str(e))

    def select_all(self):
        """ Select all users from MongoDB """
        users = self.collection.find()
        return [User(str(u["_id"]), u["name"], u["email"]) for u in users]

    def insert(self, user):
        """ Insert given user into MongoDB """
        result = self.collection.insert_one({
            "name": user.name,
            "email": user.email
        })
        return str(result.inserted_id)

    def update(self, user):
        """ Update given user in MongoDB """
        result = self.collection.update_one(
            {"_id":  ObjectId(user.id)},
            {"$set": {"name": user.name, "email": user.email}}
        )
        return result.modified_count


    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        result = self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count


    def delete_all(self): #optional
        """ Empty users table in MongoDB """
        result = self.collection.delete_many({})
        return result.deleted_count

        
    def close(self):
        self.client.close()
