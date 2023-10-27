import json
import os
from pymongo import MongoClient

# Load the data to be inserted from the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Connect to the MongoDB instance
MONGODB_URI = os.environ.get('MONGODB_URI')
client = MongoClient(MONGODB_URI)

# Select (or create) the database 'mydatabase'
db = client.surveyDB

# Select (or create) the collection 'mycollection'
collection = db.answers

# Insert each document from the loaded data
for document in data:
    collection.insert_one(document)

print("Documents inserted successfully!")

# Close the connection
client.close()
