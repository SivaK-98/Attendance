import crypt
import datetime
import pymongo
from pymongo.errors import DuplicateKeyError
import os

url = os.getenv("mongodb")
url = "mongodb+srv://awstestuser1998:awstestuser1998@cluster0.nb2lq1w.mongodb.net/"

client = pymongo.MongoClient(url)
db = client["auth"]
auth_db = db["users"]
db.users.create_index([('email', pymongo.ASCENDING)], unique=True)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("successfully connected to MongoDB!")
    response = crypt.encryptor("test")
    print(response)
    return response

except Exception as e:
    print(e)
