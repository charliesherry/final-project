from pymongo import MongoClient


dbName = "recipes"
client = MongoClient(f"mongodb://localhost/{dbName}")
db = client.get_database()
