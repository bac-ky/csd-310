
#required python code to connect to the student collection
from pymongo import MongoClient
client = MongoClient("localhost",27017)
db = client["mydb"]
pytech = db["Pytech"]
records =[

    {
    "student_id": "1007",
     "first_name": "Kyle",
     "last_name":"Teller"},

    {"student_id": "1008",
     "first_name": "Will",
     "last_name":"Carpenter"
     },
     {
     "student_id": "1009",
     "first_name": "Nancy",
     "last_name":"Brave"
      } 

] 

#3 call the find() method to Display the results. 
for records in records.find():
    print(records)

#update the student with id 1007
records.update_one({"student-id":1007, "$set":{"last_name":"Englishman"}})

print(records)

