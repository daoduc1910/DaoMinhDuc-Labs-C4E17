from pymongo import MongoClient

#1 . Connect to database server
uri = "mongodb://admin:admin@ds157639.mlab.com:57639/sheep"   #uri là đường dẫn tới database của mình
client = MongoClient(uri) #thiết lập kết nối tới database thông qua đường link này

#2. Get default database
db = client.get_default_database() #truy cập vào cái database mặc định

#3. Get blog collection
blog = db["blog"] #mở cái blog ra - nếu chưa có thì mongodb sẽ tạo cho mình 1 cái mới

#4. Write a new blog
post = {
    'title': "Hôm nay tôi buồn",
    'content': "Buồn thì ở nhà code chứ sao"
}

#blog.insert_one(post) #tạo 1 cái blog

all_post = blog.find() #trả lại cho mình 1 list các document
for post in all_post:
    print(post)
