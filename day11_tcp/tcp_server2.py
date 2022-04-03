"""
ｔｃｐ　服务端　循环模型２
重点代码　！！！　
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket()

# 绑定改地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置监听
tcp_socket.listen(5)

# 循环等待客户端连接
while True:
    print("等待连接......")
    connfd,addr = tcp_socket.accept()
    print("连接了：",addr)

    #　收发消息　：　每次连接只能收发一次消息
    data = connfd.recv(1024)
    print("收到:",data.decode())
    connfd.send(b"Thanks")

    connfd.close()

tcp_socket.close()








