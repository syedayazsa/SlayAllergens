# SlayAllergens

SlayAllergens is python tool which works on cosine similarity and correlation algorithms to provide content based and collaberative recommendations related to food items.

## Tools/Libraries Used:
```Numpy
Pandas
Pymongo
Scikit-Learn
```

## How to Download:
* To download the project, open shell ```terminal``` or ```git-bash``` and clone it to your local directory (or download the project as zip).


## How to set-up:
1. Download ```MonogoDB-community-server``` from [here](https://www.mongodb.com/download-center/community) and ```install``` it.
2. Download ```MongoDB-Compass``` from [here](https://www.mongodb.com/download-center/compass) and ```install``` it (If not already installed while installing ```MonogoDB-community-server```).
3. Open the ```terminal``` and install the required libraires.
4. Open MongoDB compass and connect by clicking on ```Fill in connection fields individually``` and then on connect.
5. Now create a new database, with database name as ```project``` and collection name as ```accounts```.
6. Open the database and you'll see a collection named ```accounts```. Now click on ```Create Collection``` to create 2 more collections in the project database. Name them ```filefood``` and ```newingredient```.
7. Goto the newly created collections and import ```filefood.csv``` to ```filefood``` collection and ```editedingredients.csv``` to ```newingredient``` collection.
8. Your database is ready now.

## How to run:
* Open ```terminal``` or ```Command Prompt``` and change directory into the ```git-clone``` or download location as:
```sh
$ cd PATH_TO_DIRECTORY
```
* Input the following command to run the project:
```sh
$ python3 main.py
```

