"""
chat room 客户端代码
"""

from socket import *
from multiprocessing import Process
import sys

# 服务器地址
ADDR = ('119.3.124.77', 8000)


# 处理登录
def login(sock):
    while True:
        # 进入聊天室
        name = input("Name:")
        # 发送姓名
        msg = "LOGIN " + name
        sock.sendto(msg.encode(), ADDR)
        # 接收结果
        result, addr = sock.recvfrom(128)
        if result.decode() == 'OK':
            print("进入聊天室")
            return name
        else:
            print("该用户已存在")


# 接收消息
def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(1024 * 10)
        msg = "\n%s\n发言：" % data.decode()
        print(msg, end="")  # 不换行


# 发送消息
def send_msg(sock, name):
    while True:
        try:
            content = input("发言：")
        except KeyboardInterrupt:
            content = "exit"
        # 输入exit表示要退出聊天室
        if content == "exit":
            msg = "EXIT " + name
            sock.sendto(msg.encode(), ADDR)
            sys.exit("您已退出聊天室")

        msg = "CHAT %s %s" % (name, content)
        # 给服务端发送聊天请求
        sock.sendto(msg.encode(), ADDR)



# 网络连接
def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(("0.0.0.0",12345)) # 地址不变化
    name = login(sock)  # 进入聊天室

    # 创建子进程 用于接收消息
    p = Process(target=recv_msg, args=(sock,))
    p.daemon = True  # 父进程退出子进程也退出
    p.start()

    send_msg(sock, name)  # 父进程发送消息


if __name__ == '__main__':
    main()
