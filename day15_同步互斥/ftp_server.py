"""
ftp文件管理服务端
多线程 tcp 并发
"""
from socket import *
from threading import Thread
import os
from time import sleep

# 服务器地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 文件库位置
FTP = "/home/tarena/FTP/"


# 实现具体的业务功能，客户端请求都在这里处理
class FTPServer(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()

    # 处理请求文件列表
    def do_list(self):
        # 判断文件库是否为空
        files = os.listdir(FTP)
        if not files:
            self.connfd.send(b"FAIL")  # 失败
        else:
            self.connfd.send(b"OK")
            sleep(0.1)
            # 一次发送所有文件名
            data = "\n".join( )
            self.connfd.send(data.encode())
            sleep(0.1)
            self.connfd.send(b"##")

    # 处理上传
    def do_put(self, filename):
        # 判断文件是否已存在
        if os.path.exists(FTP + filename):
            self.connfd.send(b"FAIL")
            return
        else:
            self.connfd.send(b"OK")
            # 接收文件
            f = open(FTP + filename, 'wb')
            while True:
                data = self.connfd.recv(1024)
                if data == b"##":
                    break
                f.write(data)
            f.close()

    # 处理下载
    def do_get(self, filename):
        try:
            f = open(FTP + filename, 'rb')
        except:
            # 文件不存在
            self.connfd.send(b"FAIL")
            return
        else:
            self.connfd.send(b"OK")
            sleep(0.1)
            # 发送文件
            while True:
                data = f.read(1024)
                if not data:
                    break
                self.connfd.send(data)
            sleep(0.1)
            self.connfd.send(b"##")
            f.close()

    # 线程启动方法
    def run(self):
        while True:
            # 接收某一个各类请求
            data = self.connfd.recv(1024).decode()
            # print(data)
            if not data or data == "EXIT":
                break
            elif data == "LIST":
                self.do_list()
            elif data[:4] == "STOR":
                filename = data.split(' ')[-1]
                self.do_put(filename)
            elif data[:4] == "RETR":
                filename = data.split(' ')[-1]
                self.do_get(filename)
        self.connfd.close()


# 函数中搭建并发结构
def main():
    sock = socket()  # tcp套接字
    sock.bind(ADDR)
    sock.listen(5)

    print("Listen the port %d" % PORT)

    while True:
        # 循环接收客户端连接
        try:
            connfd, addr = sock.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            # 退出服务
            sock.close()
            break
        # 使用自定义线程类为连接的客户端创建新线程
        t = FTPServer(connfd)
        t.setDaemon(True)  # 客户端随服务端退出
        t.start()


if __name__ == '__main__':
    main()
