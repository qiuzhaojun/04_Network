"""
基于epoll的 IO网络并发模型

IO 多路复用与非阻塞搭配

重点代码 ！！！
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

# 创建epoll对象
ep = epoll()

# 查找字典  fileno--> io object
map = {sockfd.fileno():sockfd}

# 初始监听套接字，先关注他
ep.register(sockfd,EPOLLIN)

# 循环监控IO对象
while True:
    # events --> [(fileno,event),()]
    events = ep.poll()
    print("你有新的IO需要处理哦",events)
    # 遍历events 处理就绪的IO
    for fd,event in events:
        # 分类讨论
        if fd == sockfd.fileno():
            connfd, addr = map[fd].accept()
            print("Connect from", addr)
            # 将客户端连接套接字也监控起来
            connfd.setblocking(False)
            ep.register(connfd,EPOLLIN|EPOLLET) # 设置边缘触发
            map[connfd.fileno()] = connfd # 维护字典
        # elif event == EPOLLIN:
        #     # 某个客户端发消息 connfd 就绪
        #     data = map[fd].recv(1024).decode()
        #     # 客户端退出处理
        #     if not data:
        #         ep.unregister(fd) # 不再关注
        #         map[fd].close()
        #         del map[fd] # 从字典删除
        #         continue
        #     print(data)
        #     # map[fd].send(b"OK")
        #     ep.unregister(fd)
        #     ep.register(fd, EPOLLOUT)
        # elif event == EPOLLOUT:
        #     map[fd].send(b"OK")
        #     ep.unregister(fd)
        #     ep.register(fd, EPOLLIN)


