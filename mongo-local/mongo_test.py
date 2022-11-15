from pymongo import MongoClient

mydict = { "name": "John", "address": "Highway 37" }

client = MongoClient("localhost", 27017,
                     username="mongo",
                     password="mongo")
collection = client['testdb']['testcollection']

x = collection.insert_one(mydict)
print(x)