from pymongo import MongoClient
from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_default_database()

posts = db["customers"]

ref_count = []
ref_names = ["events", "ads", "wom"]

for ref in ref_names:
    count = posts.find({'ref' : ref}).count()
    ref_count.append(count)


pyplot.pie(ref_count, labels = ref_names, autopct = "%.1f%%", shadow = True, explode = [0, 0.2, 0.1])
pyplot.axis("equal")
pyplot.title("Marketing database".upper())
pyplot.show()
