"""
chat room 客户端代码
"""

from socket import *

# 服务器地址
ADDR = ('127.0.0.1', 8000)


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
            break
        else:
            print("该用户已存在")

# 网络连接
def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    login(sock) # 进入聊天室



if __name__ == '__main__':
    main()
