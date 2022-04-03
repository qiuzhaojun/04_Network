from  socket import *

# 服务器地址
server_addr = ("127.0.0.1",8888)


# 创建tcp套接字
tcp_socket = socket()
tcp_socket.connect(server_addr)

file = open("timg.jfif",'rb') # 二进制打开

# 边读取边发送
while True:
    data = file.read(1024)
    if not data:
        break
    tcp_socket.send(data)

file.close()
tcp_socket.send(b"##")

# 接收通知
msg = tcp_socket.recv(1024)
print(msg.decode())


# 关闭套接字
tcp_socket.close()