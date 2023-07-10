from pymongo import MongoClient
client = MongoClient("localhost",27017)
db = client["Pytech"]
students = db["students"]
students= [    
     { "student_id": "1007",
       "first_name": "Kyle",
       "last_name":"Teller"
    },

    {  "student_id": "1008",
       "first_name": "Will",
       "last_name":"Carpenter"
    },

    {
      "student_id": "1009",
      "first_name": "Nancy",
      "last_name":"Brave"
    } ]
        
  
#Display all documents in the collection
for student in students.find():
    print(students)

#insert a new document
new_student={"student_id":1010,
             "first_name":"Lisa",
             "last_name":"Walker"
             }
students.insert_one(new_student)

#Display the inserted document
inserted_student=students.find_one({"student_id":1010})
print(inserted_student)

#Delete the inserted document

students.delete_one({"student_id":1010})

#Display all documents in the collection again
for student in students.find():
    print(student)
    