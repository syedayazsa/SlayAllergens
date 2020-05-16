#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:13:10 2019

@author: ayaz
"""

import getpass
from pymongo import MongoClient

myclient = MongoClient()

mydb = myclient["project"]
mycol = mydb["accounts"]

us = ps = logged = 0
username = input("Please Enter your Username: \n")

password = getpass.getpass("Enter your Password: \n")

query1 = {"username": username}
query2 = {"password": password}

doc1 = mycol.find(query1)
doc2 = mycol.find(query2)

for i in doc1:
    us = 1
for j in doc2:
    ps = 1
    
if us == 1 and ps ==1:
    print("""Logged In!\n
          Begin Your Search......."\n""")
    inp = int(input("1. Algorithm 1(Cosine Sim)\n2. Algorithm 2(Correlation Method)\n"))
    logged = 1    
else:
    print("Wrong Credentials")

if inp == 1:
    import food_cosinesim

else:
    import food_correlation
