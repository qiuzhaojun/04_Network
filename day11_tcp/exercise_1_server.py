"""
练习： 使用tcp完成，将一个图片从客户端上传的服务端
注意，图片有可能比较大，不允许一次性 read()读取
在服务端以当前日期为名字存储

2020-10-16.jpg

思路 ： 客户段读取文件内容发送
       服务端接收内容，写入文件
"""

from socket import *
from time import localtime

# 创建tcp套接字服务端
tcp_socket = socket()
tcp_socket.bind(("0.0.0.0",8888))
tcp_socket.listen(5)

# 循环接收客户端连接
while True:
    connfd,addr = tcp_socket.accept()
    # 打开一个以当前日期命名的文件
    filename = "%d-%d-%d.jpg"%localtime()[:3]
    file = open(filename,'wb')

    # 接收某一个客户端上传的图片
    while True:
        # 边收边写入
        data = connfd.recv(1024)
        if data == b'##':
            break
        file.write(data)
    file.close()

    # 发送通知
    connfd.send("上传完成".encode())

    connfd.close()

# 关闭套接字
tcp_socket.close()







