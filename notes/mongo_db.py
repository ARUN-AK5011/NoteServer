import pymongo

MONGO_URI = "mongodb+srv://ak:arun@instarental.1u95hti.mongodb.net/Notes?retryWrites=true&w=majority&appName=InstaRental"
mongo_client = pymongo.MongoClient(MONGO_URI)
db = mongo_client["Notes"] 
