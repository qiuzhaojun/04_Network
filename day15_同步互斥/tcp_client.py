from socket import *

# 服务器地址
server_addr = ("127.0.0.1",8888)

tcp_socket = socket()
tcp_socket.connect(server_addr)

# 收发消息
while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("从服务器收到:",data.decode())

tcp_socket.close()
