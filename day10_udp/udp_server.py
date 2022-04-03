"""
udp 服务端基础功能示例

重点代码 ！！！
"""

from socket import *

# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
udp_socket.bind(("0.0.0.0",8888))

# 接收消息
while True:
    data,addr = udp_socket.recvfrom(5)
    print(addr,"收到:",data.decode()) # data字节串

    # 发送消息 发送字节串
    n = udp_socket.sendto(b"Thanks",addr)
    print("发送了%d bytes"%n)

# 关闭套接字
udp_socket.close()






