import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]

df = pd.read_csv("editedIngredients.csv")

features = ['ingredients', 'brand', 'categories', 'manufacturer']


for feature in features:
    df[feature] = df[feature].fillna('')

def combine_features(row):
    return row['ingredients'] + " "+row['brand']+" "+row['categories']+" "+row["manufacturer"]

df["combined_features"] = df.apply(combine_features, axis = 1)


cv = CountVectorizer()
count_matrix=cv.fit_transform(df["combined_features"])

cosine_sim = cosine_similarity(count_matrix)
print("\n\n")
print("Search Here: ")
food_user_likes = input()

food_index = get_index_from_title(food_user_likes)
similar_food = list(enumerate(cosine_sim[food_index]))

sorted_similar_food = sorted(similar_food,key =lambda x:x[1]  ,reverse=True)


i = 0
for food in sorted_similar_food:
    print(get_title_from_index(food[0]))
    i = i+1
    if i>50:
        break