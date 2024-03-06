from pymongo import MongoClient

client = MongoClient('mongodb+srv://user254:user254@cluster0.3tm6rab.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = client.todo_db
collection_name = db.get_collection('db_collection')
