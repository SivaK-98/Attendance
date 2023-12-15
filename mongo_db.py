import crypt
import datetime
import pymongo
from pymongo.errors import DuplicateKeyError
import os

url = os.getenv("mongodb")
client = pymongo.MongoClient(url)
db = client["attendance"]
auth_db = db["users"]
db.users.create_index([('email', pymongo.ASCENDING)], unique=True)


def signup(email, roll_number, mobile, password, role):
  try:
    user_db = db[roll_number]
    created_time = datetime.datetime.now()
    encrypt_data = crypt.encryptor(password)
    encrypte_pass = encrypt_data[0]
    key = encrypt_data[1]
    query = {
        "email": email,
        "mobile": mobile,
        "password": encrypte_pass,
        "key": key,
        "roll_number": roll_number,
        "created_time": created_time
    }
    auth_db.insert_one(query)
    query2 = {
        "hour_1": "",
        "hour_2": "",
        "hour_3": "",
        "hour_4": "",
        "hour_5": "",
        "hour_6": "",
        "hour_7": "",
        "hour_8": "",
    }
    user_db.insert_one(query2)
    return True
  except DuplicateKeyError:
    print("Duplicate ID not allowed")
    return "duplicate"
