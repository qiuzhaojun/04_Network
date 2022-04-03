"""
tcp 客户端 基础示例
"""
from  socket import *

# 服务器地址
server_addr = ("127.0.0.1",8888)


# 创建tcp套接字
tcp_socket = socket()

# 连接服务器
tcp_socket.connect(server_addr)

# 收发消息
msg = input(">>")
tcp_socket.send(msg.encode())
data = tcp_socket.recv(1024)
print("从服务器收到:",data.decode())

# 关闭套接字
tcp_socket.close()



