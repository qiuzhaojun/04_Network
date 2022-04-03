from socket import *

# 服务端地址
ADDR = ("172.40.91.108",8888)

# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 发送内容
while True:
    word = input("Word:")
    # msg为空 则退出循环
    if not word:
        break

    udp_socket.sendto(word.encode(),ADDR)

    # 接收服务器发来的解释
    data,addr = udp_socket.recvfrom(1024)
    print("%s : %s"%(word,data.decode()))

udp_socket.close()