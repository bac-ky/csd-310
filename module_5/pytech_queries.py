from traceback import print_tb
from pymongo import MongoClient
client = MongoClient("localhost",27017)
db = client["mydb"]
pytech = db["Pytech"]
records = [  

    {  "student_id": "1007",
     "first_name": "Kyle"
     "last_name":"Teller"
     },

    {"student_id": "1008",
     "first_name": "Will"
     "last_name":"Carpenter"
     },
     {
     "student_id": "1009",
     "first_name": "Nancy"
     "last_name":"Brave"
      } 
]
    


doc = pytech.find()
print_tb(doc)

print(pytech.find_one({"student_id": "1007"}))





