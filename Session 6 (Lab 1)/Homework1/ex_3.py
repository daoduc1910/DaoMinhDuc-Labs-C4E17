from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_default_database()

blog = db["posts"]

post = {
    "title" : "Tương tư",
    "author": "Vương Duy",
    "content":  '''
                Hồng đậu sinh nam quốc,
                Xuân lai phát kỷ chi.
                Nguyện quân đa thái hiệt,
                Thử vật tối tương tư.
                '''
}

blog.insert_one(post)
