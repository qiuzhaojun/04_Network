"""
poll IO 多路复用方法
"""
from socket import *
from select import *

# 制作一些IO对象
file = open("my.log",'a+')

sock_tcp = socket()
sock_tcp.bind(("0.0.0.0",8888))
sock_tcp.listen(5)

sock_udp = socket(AF_INET,SOCK_DGRAM)

#　查找字典　需要与ｒｅｇｉｓｔｅｒ的ＩＯ保持一直
map = {sock_tcp.fileno():sock_tcp,
       sock_udp.fileno():sock_udp,
       file.fileno():file}

# 准备poll方法
p = poll() # 生成poll对象
p.register(sock_tcp,POLLIN|POLLERR)
p.register(sock_udp,POLLOUT)
p.register(file,POLLOUT)

print("开始监控IO")
events = p.poll()

# events --> [(fileno,event),()]
# 必须获取到IO对象才能调用方法处理IO
print(events)
