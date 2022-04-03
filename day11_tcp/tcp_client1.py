"""
tcp 客户端 循环实例
重点代码 ！！！
"""
from  socket import *

# 服务器地址
server_addr = ("127.0.0.1",8888)


# 创建tcp套接字
tcp_socket = socket()

# 连接服务器
tcp_socket.connect(server_addr)

# 收发消息
while True:
    msg = input(">>")
    # 直接回车msg为空
    if not msg:
        break

    tcp_socket.send(msg.encode())
    # 发送##告知服务端自己退出
    # if msg == "##":
    #     break
    data = tcp_socket.recv(1024)
    print("从服务器收到:",data.decode())

# 关闭套接字
tcp_socket.close()
