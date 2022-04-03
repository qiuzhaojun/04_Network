"""
dict 服务端
* 接收请求
* 逻辑处理
* 将数据整合给客户端
"""
from socket import *
from multiprocessing import Process
from signal import *
from dict_db import *
from time import sleep

# 服务器地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 实例化数据库处理对象
db = Database()

# 处理注册
def do_register(connfd,name,passwd):
    # register --> True False
    if db.register(name,passwd):
        connfd.send(b"OK")
    else:
        connfd.send(b"FAIL")

# 处理登录
def do_login(connfd,name,passwd):
    # login --> True False
    if db.login(name,passwd):
        connfd.send(b"OK")
    else:
        connfd.send(b"FAIL")

# 处理单词查询
def do_query(connfd,name,word):
    # 返回单词解释
    mean = db.query(word)
    data = "%s : %s"%(word,mean)
    connfd.send(data.encode()) # 给客户端
    # 插入历史记录
    db.insert_history(name,word)

# 查询历史记录
def do_history(connfd,name):
    # result -> ((name,word,time),()....)
    result = db.history(name)
    for row in result:
        # row -> (name,word,time)
        msg = "%s     %s    %s"%row
        connfd.send(msg.encode())
        sleep(0.1)
    connfd.send(b"##")

# 处理客户端各种请求  总分结构
def handle(connfd):
    db.create_cursor() # 每个子进程创建自己的游标
    while True:
        # 接收某一个各类请求
        data = connfd.recv(1024).decode()
        # 简单解析
        tmp = data.split(' ')
        if not data or tmp[0] == 'E':
            break
        elif tmp[0] == "R":
            # tmp --> [R,name,passwd]
            do_register(connfd,tmp[1],tmp[2])
        elif tmp[0] == "L":
            # tmp --> [L,name,passwd]
            do_login(connfd,tmp[1],tmp[2])
        elif tmp[0] == "Q":
            # tmp --> [Q,name,word]
            do_query(connfd,tmp[1],tmp[2])
        elif tmp[0] == "H":
            # tmp --> [H,name]
            do_history(connfd,tmp[1])

    db.cur.close() # 关闭游标
    connfd.close()


# 在这个函数中进行并发网络服务搭建
def main():
    sock = socket()  # tcp套接字
    sock.bind(ADDR)
    sock.listen(5)

    print("Listen the port %d" % PORT)
    signal(SIGCHLD, SIG_IGN)  # 处理僵尸进程

    while True:
        # 循环接收客户端连接
        try:
            connfd, addr = sock.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            # 退出服务
            sock.close()
            db.close()
            break
        # 为连接的客户端创建新进程
        p = Process(target=handle, args=(connfd,))
        p.daemon = True  # 客户端随服务端退出
        p.start()


if __name__ == '__main__':
    main()