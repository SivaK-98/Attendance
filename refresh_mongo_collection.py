import pymongo
import csv


url = "mongodb+srv://awstestuser1998:awstestuser1998@cluster0.nb2lq1w.mongodb.net/"
client = pymongo.MongoClient(url)
db = client["pivot_data"]
db.segment.drop()
with open('students.csv', 'r') as csvfile:
  header = ["Name", "Email", "Enroll_number", "Department", "Year", "Role"]
  reader = csv.reader(csvfile)

  for row in reader:
    doc = {}
    for n in range(0, len(header)):
      doc[header[n]] = row[n]

    db.segment.insert_many(doc)
