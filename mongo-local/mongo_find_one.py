from pymongo import MongoClient


client = MongoClient("localhost", 27017,
                     username="mongo",
                     password="mongo")
collection = client['testdb']['testcollection']

x = collection.find_one()
print(x)