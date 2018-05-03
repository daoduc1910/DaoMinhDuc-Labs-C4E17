from gmail import *
from random import *


html_template = '''<p>Xin ch&agrave;o,</p>
<p>H&ocirc;m nay {{S}} cảm thấy rất {{sickness}}. N&ecirc;n anh cho ph&eacute;p em nghỉ l&agrave;m với ạ!</p>'''

sickness_list = ["Thương hàn", "Kiết lị", "Ebola"]

sickness = choice(sickness_list)

gmail = GMail('Ngô Quang Trường<minhthao12121998@gmail.com>','0966819573')

html_content = html_template.replace("{{sickness}}", sickness).replace("{{S}}", "anh") #dùng hàm replace để thay thế tất cả các từ {{sickness}} bằng từ thương hàn

#text chỉ gửi 1 đoạn văn bản - mà mình muốn đoạn văn bản xanh đỏ ... thì phải dùng HTML
# msg = Message('Test Message', to ='daoduc1910@gmail.com',text = "Hello")
msg = Message('Test message', to ='daoduc1910@gmail.com', html = html_content)
#Message('Tiêu đề', to ='địa chỉ đến', text = 'nội dung' )

gmail.send(msg)

#yêu cầu về nhà: cứ 7h là gửi email xong thoát
