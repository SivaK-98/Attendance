import crypt
import datetime
import os

import pymongo
from pymongo.errors import DuplicateKeyError

url = os.getenv("MONGODB")

mongo_client = pymongo.MongoClient(url)
db = mongo_client["attendance"]
member_db = db["members"]
db.members.create_index([('email', pymongo.ASCENDING)], unique=True)


def signup(name,email, phone, register, roll, password):
    email = email
    phone = phone
    reigster = register
    roll = roll
    encrypted = crypt.encryptor(password)
    encrypted_pass = encrypted[0]
    key = encrypted[1]
    query = {
        "email": email,
        "phone": phone,
        "register": register,
        "roll": roll,
        "password": encrypted_pass,
        "key": key
    }
    try:
        insert = member_db.insert_one(query)
        return "Success"
    except Exception as err:
        return err
