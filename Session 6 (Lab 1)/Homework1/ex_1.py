from gmail import *
from datetime import *

now = datetime.now()
html_content = '''<p>H&ocirc;m nay l&agrave; một ng&agrave;y đẹp trời,
em đang bị Ebola n&ecirc;n em viết đơn nay xin ph&eacute;p anh cho em nghỉ học h&ocirc;m nay với ạ!!</p>'''

loop = True
while loop:
    if now.hour == 7 and now.minute == 00:

        gmail = GMail('Ngô Quang Trường<minhthao12121998>','0966819573')
        msg = Message('Xin nghỉ học',to = 'quangtruong23121996@gmail.com', html = html_content)
        gmail.send(msg)

        loop = False
