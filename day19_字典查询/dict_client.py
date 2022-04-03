"""
dict 客户端
"""
from socket import *

# 服务器
ADDR = ("0.0.0.0", 8888)


def do_query(sockfd, name):
    while True:
        word = input("Word:")
        if word == "##":
            break
        msg = "Q %s %s" % (name, word)
        # 发送请求
        sockfd.send(msg.encode())
        # 服务端无论是否查询到都返回要打印的内容
        result = sockfd.recv(1024).decode()
        print(result)

# 获取历史记录
def do_history(sockfd,name):
    msg = "H "+ name
    sockfd.send(msg.encode()) # 发送请求
    # 循环接收历史记录
    while True:
        data = sockfd.recv(1024).decode()
        if data == '##':
            break
        print(data)

# 二级界面
def login(sockfd, name):
    # 二级界面
    while True:
        print("""
        ============ 查询界面 ===============
          1. 查单词   2. 历史记录   3. 注销
        ==========================User:%s===
        """ % name)
        cmd = input("请输入命令:")

        if cmd == "1":
            do_query(sockfd, name)
        elif cmd == '2':
            do_history(sockfd,name)
        elif cmd == '3':
            break  # 退出二级界面
        else:
            print("请输入正确命令")


# 请求注册
def do_register(sockfd):
    while True:
        name = input("User:")
        passwd = input("Passwd:")

        if " " in name or ' ' in passwd:
            print("用户名密码不许有空格")
            continue

        # 组织请求
        msg = "R %s %s" % (name, passwd)
        sockfd.send(msg.encode())
        # 等待结果
        result = sockfd.recv(1024).decode()
        # 分情况讨论
        if result == "OK":
            print("注册成功")
        else:
            print("该用户已存在")
        return


def do_login(sockfd):
    name = input("User:")
    passwd = input("Passwd:")

    # 组织请求
    msg = "L %s %s" % (name, passwd)
    sockfd.send(msg.encode())
    # 等待结果
    result = sockfd.recv(1024).decode()
    # 分情况讨论
    if result == "OK":
        print("登录成功")
        login(sockfd, name)  # 进二级界面
    else:
        print("用户名或密码错误")


# main启动服务
def main():
    # 连接服务端
    sockfd = socket()
    sockfd.connect(ADDR)

    # 一级界面
    while True:
        print("""
        ============ 登录界面 =============
          1. 注册     2. 登录     3. 退出
        ==================================
        """)
        cmd = input("请输入命令:")
        if cmd == "1":
            do_register(sockfd)
        elif cmd == '2':
            do_login(sockfd)
        elif cmd == '3':
            sockfd.send(b"E")
            sockfd.close()
            break
        else:
            print("请输入正确命令")


if __name__ == '__main__':
    main()
