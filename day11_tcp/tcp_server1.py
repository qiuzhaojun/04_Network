"""
tcp 服务端循环实例1
重点代码 ！！！
"""

from socket import *
from time import sleep

# 创建tcp套接字 (不写参数默认也是tcp)
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定改地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置监听
tcp_socket.listen(5)

# 循环等待客户端连接
while True:
    print("等待连接......")
    connfd,addr = tcp_socket.accept()
    print("连接了：",addr)

    # 循环与某一个客户端收发消息
    while True:
        data = connfd.recv(5)
        # 客户端断开连接，此时recv返回空字节串
        if not data:
            break
        # 收到了## 表示客户端已经退出
        # if data == b"##":
        #     break
        print("接收到:",data.decode())
        connfd.send(b"Thanks#")
        # sleep(0.1)
    connfd.close() # 断开连接

# 关闭套接字
tcp_socket.close()








