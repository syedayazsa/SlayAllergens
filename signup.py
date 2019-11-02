#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:00:33 2019

@author: ayaz
"""
import getpass
from pymongo import MongoClient

myclient = MongoClient()

mydb = myclient["project"]
mycol = mydb["accounts"]


print("Username: ")
username = input()

for i in mycol.find({},{ "_id":0, "username": 1 }):
  string = str(i)
  string = string[14:21]
  if(username == string):
      print("The username already exits please choose another one!")
      print("Username: ")
      username = input()

print("Name: ")
name = input()

print("email: ")
email = input()

password = getpass.getpass('Enter your Password: ')

print("address: ")
address = input()


print("""
    1. GLUTEN
    2. SOY
    3. MILK/LACTOSE
    4. EGG
    5. NUTS      
""")
allergytype = input()
if(allergytype ==  1):
    allergy = "gluten"
elif(allergytype == 2):
    allergy = "soy"
elif(allergytype == 3):
    allergy = "milk/lactose"
elif(allergytype == 4):
    allergy = "egg"
else:
    allergy = "nut"

mydict = { "username": username,"name": name, "email": email, "address": address, "allergytype": allergytype, "password": password}
x = mycol.insert_one(mydict)
