import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["db_test"]
mycol = mydb["test_collection"]
