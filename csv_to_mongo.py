import csv
import os

import pandas as pd
import pymongo
from pymongo.errors import DuplicateKeyError

url = os.getenv("MONGODB")
mongo_client = pymongo.MongoClient(url)

db = mongo_client["attendance"]
member_db = db["members"]
db.members.create_index([('email', pymongo.ASCENDING)], unique=True)

#CSV to JSON Conversion
header = [
    "Name", "Department", "Academic Year", "Register Number", "Mobile", "Email"
]
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for items in reader:
        row = {}
        members = []
        for field in header:
            row[field] = items[header.index(field)]
            members.append(row)

#print(members)
queried_users = []
for users in member_db.find():
    queried_users.append(users)


"""
if members not in queried_users:
    for member in members:
        try:
            member_db.insert_one(member)
        except DuplicateKeyError:
            print("Member already inserted")
"""
