"""
tcp 服务端基础示例
"""

from socket import *

# 创建tcp套接字 (不写参数默认也是tcp)
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定改地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置监听
tcp_socket.listen(5)

# 等待客户端连接
print("等待连接......")
connfd,addr = tcp_socket.accept()
print("连接了：",addr)

# 收发消息
data = connfd.recv(1024)
print("接收到:",data.decode())

connfd.send(b"Thanks")

# 关闭套接字
connfd.close() # 断开连接
tcp_socket.close()

