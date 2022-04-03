"""
基于select的 IO网络并发模型

IO 多路复用与非阻塞搭配

重点代码 ！！！
"""
from socket import *
from select import select

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

# 初始只有监听套接字，先关注他
rlist = [sockfd]  # 客户端连接
wlist = []
xlist = []

# 循环监控IO对象
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    # 处理就绪的IO
    for r in rs:
        # 有客户端连接
        if r is sockfd:
            connfd, addr = r.accept()
            print("Connect from", addr)
            # 将客户端连接套接字也监控起来
            connfd.setblocking(False)
            rlist.append(connfd)
        else:
            # 某个客户端发消息 connfd 就绪
            data = r.recv(1024).decode()
            # 客户端退出处理
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data)
            # r.send(b"OK")
            wlist.append(r) # 存入写列表

    for w in ws:
        w.send(b"OK")
        wlist.remove(w) # 写完要移除要不一直写

    for x in xs:
        pass








