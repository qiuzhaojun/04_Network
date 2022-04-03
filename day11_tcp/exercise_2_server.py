"""
练习2: 编写一个程序，启动服务端后 作为对话机器人
小美。 客户端可以输入问题给小美，小美做出回答
如果没有找到答案则回复 “人家还小不知道”

要求，可以多个客户端一起启动
"""
from socket import *
import re

CHAT_FILE = "./chat.txt"
chat = [] # [(key,answer)]

# 提取文件中的内容，放在列表中
def answer():
    # 打开对话文件
    file = open(CHAT_FILE)
    for line in file:
        # 匹配出关键词和答案
        tup = re.findall(r"(\w+)\s+(.*)",line)
        chat.extend(tup) # 列表的合并
    file.close()

# 找答案
def find(q):
    for key,value in chat:
        # 如果关键词在问题中
        if key in q:
            return value # 返回准备的答案
    return "人家还小不知道啦！"


def main():
    answer() # 生成列表

    # 创建监听套接字
    tcp_socket = socket()
    tcp_socket.bind(("0.0.0.0", 8888))
    tcp_socket.listen(5)

    # 循环等待客户端连接
    while True:
        print("等待问题......")
        connfd, addr = tcp_socket.accept()

        # 接收问题
        data = connfd.recv(1024)
        # 找答案
        value = find(data.decode())
        connfd.send(value.encode())
        connfd.close()

    tcp_socket.close()


if __name__ == '__main__':
    main()
