"""
非阻塞IO实例
"""

from socket import *

s = socket()
s.bind(("0.0.0.0",8888))
s.listen(5)

# 设置为非阻塞
s.setblocking(False)

while True:
    try:
        c,addr = s.accept()
        print("Connect from ",addr)
    except BlockingIOError as e:
        print("干点别的")
    else:
        data = c.recv(1024)
        print(data.decode())