from pymongo import MongoClient

MONGO_URI = "mongodb+srv://Juan:FxoxPzAdtU1VTMWG@medicare.dzxx3ki.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client['Medicare']
