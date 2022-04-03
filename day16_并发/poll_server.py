"""
基于poll的 IO网络并发模型

IO 多路复用与非阻塞搭配
"""
from socket import *
from select import *

# 网络地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

# 创建监听套接字
sockfd = socket()
sockfd.bind(ADDR)
sockfd.listen(5)

# 设置非阻塞
sockfd.setblocking(False)

# 创建poll对象
p = poll()

# 查找字典  fileno--> io object
map = {sockfd.fileno():sockfd}

# 初始监听套接字，先关注他
p.register(sockfd,POLLIN)

# 循环监控IO对象
while True:
    # events --> [(fileno,event),()]
    events = p.poll()
    # 遍历events 处理就绪的IO
    for fd,event in events:
        # 分类讨论
        if fd == sockfd.fileno():
            connfd, addr = map[fd].accept()
            print("Connect from", addr)
            # 将客户端连接套接字也监控起来
            connfd.setblocking(False)
            p.register(connfd,POLLIN|POLLERR)
            map[connfd.fileno()] = connfd # 维护字典
        elif event == POLLIN:
            # 某个客户端发消息 connfd 就绪
            data = map[fd].recv(1024).decode()
            # 客户端退出处理
            if not data:
                p.unregister(fd) # 不再关注
                map[fd].close()
                del map[fd] # 从字典删除
                continue
            print(data)
            # map[fd].send(b"OK")
            p.register(fd,POLLOUT)
        elif event == POLLOUT:
            map[fd].send(b"OK")
            p.register(fd,POLLIN)









