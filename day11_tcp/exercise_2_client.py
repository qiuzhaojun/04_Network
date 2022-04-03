from  socket import *

# 服务器地址
server_addr = ("127.0.0.1",8888)


# 所有连接操作 和数据操作 全在循环中
while True:
    msg = input("我:")
    if not msg:
        break

    tcp_socket = socket()
    tcp_socket.connect(server_addr)
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("小美:",data.decode())
    tcp_socket.close()