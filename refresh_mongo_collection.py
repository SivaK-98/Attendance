import pymongo
import csv

with open('data.csv', 'r') as csvfile:
  header = [ "show_id", "director"]
  reader = csv.reader(csvfile)

  for row in reader:
      doc={}
      for n in range(0,len(header)):
          doc[header[n]] = row[n]

      db.foo.insert(doc)
Share
Improve this answer
Follow