"""
套接字使用基础示例
"""
import socket

# 创建一个UDP套接字
udp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM)

"""
1. 127.0.0.1 或者 localhost 那么 另外一端只能在
同一个计算机上通过127.0.0.1 访问之

2. 绑定自己的网络IP地址，那么另外一端可以在任何位置
通过 该主机IP地址访问之

3. 绑定自己的网络0.0.0.0地址，那么另外一端可以在
同一计算机上使用127.0.0.1访问之 或者 在任何位置
通过IP地址访问之
"""

udp_socket.bind(("172.40.91.108",8800))

