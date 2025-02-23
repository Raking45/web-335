"""
Title: king_usersp2.py
Author: Robert King
Date: February 23, 2025
Description: Python program that connects to MongoDB database and performs various operations.
"""
#Install pymongo (pip -m pip install pymongo)
#Import the MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime


#Create connection string
uri = "mongodb+srv://web335_user:s3cret@bellevueuniversity.7gku3.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity"

#Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

#Configure a variable to access the web335DB
db = client['web335DB']


#Send a ping to confirm a successful connection
try:
  client.admin.command('ping')
  #Utilize empty print() statements to add appropriate whitespace.
  print()
  print("Pinged your deployment. You have successfully connected to MongoDB!")
except Exception as e:
  print(e)

# Create a New User Document
vannoy = {
  "firstName":"Jesica",
  "lastName":"Vannoy",
  "employeeId":"1018",
  "email":"jvannoy@me.com",
  "dateCreated": datetime.now().isoformat()
}

# Insert the New User Document into Users Collection
vannoy_user_id = db.users.insert_one(vannoy).inserted_id
print(vannoy_user_id)
print()

# Prove the Insert Worked
print("New User Created Verification: ")
print(db.users.find_one({"employeeId":"1018"}))
print()

# Update the Email Address of User
db.users.update_one(
  {"employeeId": "1018"},
  {
    "$set":{"email":"jesica.vannoy@me.com"
    }
  }
)

# Prove the Update Worked
print("User Email Update Verification: ")
print(db.users.find_one({"employeeId":"1018"}))
print()

# Delete a User
result = db.users.delete_many({"employeeId":"1018"})

# Display the Results
print(result.deleted_count)
print()

# Prove the Delete Worked
print("Deleted User Verification: ")
print(db.users.find_one({"employeeId":"1018"}))
print()