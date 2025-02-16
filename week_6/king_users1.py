"""
Title:
Author:
Date:
Description:
"""
#Install pymongo (pip -m pip install pymongo)
#Import the MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from rich.console import Console

#Create connection string
uri = "mongodb+srv://web335_user:s3cret@bellevueuniversity.7gku3.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity"

#Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

#Configure a variable to access the web335DB
db = client['web335DB']

#Declare console variable for bold print
console = Console()

#Send a ping to confirm a successful connection
try:
  client.admin.command('ping')
  #Utilize empty print() statements to add appropriate whitespace.
  print()
  console.print("[bold]Pinged your deployment. You have successfully connected to MongoDB![/bold]")
except Exception as e:
  print(e)

#Call the find function to display all users in the collection
print()
console.print("[bold]Display all users in the collection.[/bold]\n")
for user in db.users.find({}):
  print(user)
  
#Use projections to only show the first and last names 
print()
console.print("[bold]Display all users in the collection by firstName & lastName only.[/bold]\n") 
for user in db.users.find({}, { "firstName": 1, "lastName": 1 }):
  print(user)
  
#Call the find_one function to display a user document by ID
print()
console.print("[bold]Find a single user by employeeId (1011).[/bold]\n")
print(db.users.find_one({ "employeeId" : "1011" }))
print()

#Call the find_one function to display a user document by lastName
console.print("[bold]Find a single user by lastName (Mozart).[/bold]\n")
print(db.users.find_one({ "lastName" : "Mozart" }))
#Whitespace between program and command line.
print()