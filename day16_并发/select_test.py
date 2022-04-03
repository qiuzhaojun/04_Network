"""
select IO 多路复用方法
"""
from socket import *
from select import select

# 制作一些IO对象
file = open("my.log",'a+')

sock_tcp = socket()
sock_tcp.bind(("0.0.0.0",8888))
sock_tcp.listen(5)

sock_udp = socket(AF_INET,SOCK_DGRAM)

# 监控IO
print("开始监控IO")
rs,ws,xs = select([],[sock_udp,file],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)