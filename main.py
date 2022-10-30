import pymongo

print("wlcome to survey program")
client=pymongo.MongoClient("mongodb://localhost:27017")
print(client)
db=client['GithubRepo']
collection=db['mydata']
na=input("Enter your name: ")
em=input("Enter your email: ")
rev=input("enter your review about this repository")

dic={'name':na , 'email':em , 'review': rev}
collection.insert_one(dic)

