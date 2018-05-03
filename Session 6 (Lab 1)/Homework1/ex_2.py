from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_default_database

blog = db["posts"]

all_post = blog.find()

for post in all_post:
    print(post)
