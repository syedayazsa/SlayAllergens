#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 13:43:58 2019

@author: ayaz
"""

import pandas as pd
import pymongo
import numpy as np
from pymongo import MongoClient

client = MongoClient()

#getting the data
db = client.project
collection = db.filefood
df = pd.DataFrame(list(collection.find()))
del df['_id']
df.columns = ['rating','item_id','user_id']

#Importing food and thier respective IDs
collection = db.newingredient
food_titles = pd.DataFrame(list(collection.find()))
del food_titles['_id']

#Merging df and food_titles by item id
data = pd.merge(df, food_titles, on = 'item_id')

#Converting the values into numeric
data['rating'] = pd.to_numeric(data['rating'])
data['item_id'] = pd.to_numeric(data['item_id'])
data['user_id'] = pd.to_numeric(data['user_id'])

"""#Calculate mean ratings and count of all food Products
data.groupby('title')['rating'].mean().sort_values(ascending = False)
data.groupby('title')['rating'].count().sort_values(ascending=False)"""
#Creating dataframe with 'rating' count values
ratings = pd.DataFrame(data.groupby('title')['rating'].mean())
ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())

#Sorting values according to the 'num of rating column' 
ratings.sort_values('num of ratings', ascending = False).head(10)
foodmat = data.pivot_table(index ='user_id', 
              columns ='title', values ='rating')

# analysing correlation with similar food

item = input("Enter the name of the food item: \n")
item_user_ratings = foodmat[item]

# analysing correlation with similar food 
similar_to_item = foodmat.corrwith(item_user_ratings) 


corr_item = pd.DataFrame(similar_to_item, columns =['Correlation']) 
corr_item.dropna(inplace = True)

corr_item = corr_item.join(ratings['num of ratings']) 
corr_item[corr_item['num of ratings']>100].sort_values('Correlation', ascending = False).head() 

corr_item = corr_item.sort_values('Correlation', ascending = False)

#Printing the output
print(corr_item.iloc[:,0].head(25))
