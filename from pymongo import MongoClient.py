from pymongo import MongoClient

# Replace with your MongoDB Atlas connection string
client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/test")

db = client["week5_db"]       # Database
collection = db["users"]      # Collection

# Insert 3 users
users = [
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 28}
]

collection.insert_many(users)

# Fetch all users
for user in collection.find():
    print(user)