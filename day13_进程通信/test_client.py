from socket import *

# 服务器地址
ADDR = ('127.0.0.1',8000)

# 网络连接
def main():
    sock = socket(AF_INET,SOCK_DGRAM)
    sock.sendto(b"test...",ADDR)
    while True:
        # 进入聊天室
        name = input('输入姓名')
        msg = "LOGIN " + name
        # 发送请求
        sock.sendto(msg.encode(),ADDR)
        result,addr = sock.recvfrom(128)
        if result.decode() == 'OK':
            print('进入聊天室')
        else:
            print('该用户已存在')

if __name__ == '__main__':
    main()