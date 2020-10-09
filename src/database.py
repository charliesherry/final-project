from pymongo import MongoClient


dbName = "fridge"
client = MongoClient(f"mongodb://localhost/{dbName}")
db = client.get_database("fridge")
