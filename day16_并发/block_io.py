"""
非阻塞IO实例
"""

from socket import *
from time import sleep,ctime

log = open("my.log",'a') # 打开一个日志

s = socket()
s.bind(("0.0.0.0",8888))
s.listen(5)

# 设置为非阻塞
# s.setblocking(False)

# 设置超时检测
s.settimeout(3)

while True:
    try:
        c,addr = s.accept()
        print("Connect from ",addr)
    except timeout as e:
        print("发生超时")
        msg = "%s : %s\n" % (ctime(), e)
        log.write(msg)
        log.flush()
    except BlockingIOError as e:
        print("非阻塞日志")
        sleep(2)
        msg = "%s : %s\n"%(ctime(),e)
        log.write(msg)
        log.flush()
    else:
        data = c.recv(1024)
        print(data.decode())