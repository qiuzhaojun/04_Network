"""
多进程网络并发模型
重点代码 ！！！

创建网络套接字用于接收客户端请求
等待客户端连接
客户端连接，则创建新的进程具体处理客户端请求
主进程继续等待其他客户端连接
如果客户端退出，则销毁对应的进程
"""
from socket import *
from multiprocessing import Process
from signal import *

# 服务器地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)


# 实现具体的业务功能，客户端请求都在这里处理
def handle(connfd):
    # 与客户端配合测试
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b"ok")
    connfd.close()


# 函数中编写并发服务
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
            break
        # 为连接的客户端创建新进程
        p = Process(target=handle, args=(connfd,))
        p.daemon = True  # 客户端随服务端退出
        p.start()


if __name__ == '__main__':
    main()
