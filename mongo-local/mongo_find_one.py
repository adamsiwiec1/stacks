from pymongo import MongoClient


mg = MongoClient("100.114.236.49", 27017,
                     username="mongo",
                     password="mongo")
collection = mg['stockdb']['demo']

# x = collection.find_one()
# print(x)

for x in collection.find():
    print(x)
