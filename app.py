import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['dope']
collection = database['students']

students = [students for students in collection.find({})]


print(students)