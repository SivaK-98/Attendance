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
        "role": role,
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


def login(email, password):
  try:
    result = auth_db.find_one({"email": email}, {"_id": 0})
    #print("Result from mongo DB", result)
    if result != None:
      key = result['key']
      got_password = result["password"]
      role = result["role"]
      data_pass = (got_password, key)
      decrypted = crypt.decrypt(data_pass)
      flag = False
      if decrypted == password:
        print("Password matched!!")
        flag = True
        flag = str(flag)
        account_id = result["roll_number"]
        user_db = db[str(account_id)]
        data = {"account_id": account_id, "role": role}
        print(data)
        return data
      else:
        return "Invalid email / password"
  except Exception as e:
    print(e)
    return e

def add_staff(name, email,roll_number,mobile,role):
  collection = db["staff_collections"]
  db.staff_collections.create_index([('email', pymongo.ASCENDING)], unique=True)
  try:
    query = {
        "name": name,
        "email": email,
        "roll_number": roll_number,
        "mobile": mobile,
        "role": role
    }
    collection.insert_one(query)
    return True
  except Exception as e:
    print(e)
    return e

def add_student(name, email,roll_number,mobile,role):
  collection = db["student_collections"]
  db.staff_collections.create_index([('email', pymongo.ASCENDING)], unique=True)
  try:
    query = {
          "name": name,
          "email": email,
          "roll_number": roll_number,
          "mobile": mobile,
          "role": role
      }
    collection.insert_one(query)
    return True
  except Exception as e:
    print(e)
    return e
  
   