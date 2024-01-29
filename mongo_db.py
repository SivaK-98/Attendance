import crypt
import datetime
import pymongo
from pymongo.errors import DuplicateKeyError
import os

url = os.getenv("mongodb")
client = pymongo.MongoClient(url)
db = client["attendance"]
pivot_data = db["pivot_collection"]
auth = db["auth"]
db.auth.create_index([('email', pymongo.ASCENDING)], unique=True)


def signup(data):
  try:
    print("Data:", data)
    email = data["email"]
    print(email)
    roll = data["roll"]
    name = data["name"]
    find_query = {"email": email, "roll": roll, "name": name}
    db_entry = pivot_data.find_one(find_query)
    print("DB Entry:", db_entry)
    if db_entry:
      print("DB Entry:", db_entry)
      db_entry_name = db_entry["name"]
      db_entry_email = db_entry["email"]
      db_entry_roll = db_entry["roll"]
      if db_entry_email == email and db_entry_roll == roll and db_entry_name == name:
        flag = True
        user_db = db[str(roll)]
        encrypt_data = crypt.encryptor(data["password"])
        encrypte_pass = encrypt_data[0]
        key = encrypt_data[1]
        data["role"] = db_entry["role"]
        data["password"] = encrypte_pass
        data["key"] = key
        auth.insert_one(data)
        query2 = {
            "hour_1": "P",
            "hour_2": "P",
            "hour_3": "P",
            "hour_4": "P",
            "hour_5": "P",
            "hour_6": "P",
            "hour_7": "P",
            "hour_8": "P"
        }
        user_db.insert_one(query2)
        return True
      else:
        flag = False
        return "error"
    else:
      return "No entry"
  except DuplicateKeyError:
    print("Duplicate ID not allowed")
    return "error"


def login(email, password):
  try:
    result = auth.find_one({"email": email}, {"_id": 0})
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
        roll = result["roll"]
        user_db = db[str(roll)]
        data = {"roll": roll, "role": role,"error":None}
        print(data)
        return data
      else:
        data = {"roll": None, "role": None,"error":"Password Not matched"}
        return data
  except Exception as e:
    data = {"roll": None, "role": None,"error":e}
    print(e)
    return data


def add_staff(name, email, roll_number, mobile, role):
  collection = db["staff_collections"]
  db.staff_collections.create_index([('email', pymongo.ASCENDING)],
                                    unique=True)
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


def add_student(name, email, roll_number, mobile, role):
  collection = db["student_collections"]
  db.staff_collections.create_index([('email', pymongo.ASCENDING)],
                                    unique=True)
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
