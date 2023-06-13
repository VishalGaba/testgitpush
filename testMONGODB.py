import pymongo

client = pymongo.MongoClient("mongodb+srv://vishalgaba:gabaji123A@cluster0.8njofih.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

# password should not include @ or special characters, otherwise it will give error.

d= {
    "name" : "vishalgaba",
    "email" : "er.vishal@gmail.com",
    "mobile" : "9467847292"
}

db1 = client['mongotest']
coll = db['test']
coll.insert_one(d)
