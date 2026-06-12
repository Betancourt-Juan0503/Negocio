from pymongo import MongoClient

# Tu conexión real con tu contraseña
MONGO_URI = "mongodb+srv://Juan:FxoxPzAdtU1VTMWG@medicare.dzxx3ki.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client['Medicare'] # Tu base de datos 'medicare'