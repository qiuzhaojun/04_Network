"""
ftp 文件服务 客户端
c / s  连接   发请求   获取结果
"""
from socket import *
import sys
from time import sleep

# 服务端地址
ADDR = ("127.0.0.1", 8888)


# 发起请求的所有功能
class FTPClient:
    def __init__(self, sock):
        self.sock = sock

    # 请求文件列表
    def do_list(self):
        self.sock.send(b"LIST")  # 发送请求
        result = self.sock.recv(128).decode()  # 等回复
        # 根据不同结果分情况处理
        if result == "OK":
            # 接收文件列表
            while True:
                file = self.sock.recv(1024).decode()
                if file == '##':
                    break
                print(file)
        else:
            print("文件库为空")

    # 退出
    def do_exit(self):
        self.sock.send(b"EXIT")
        self.sock.close()
        sys.exit("谢谢使用")

    # 处理上传
    def do_put(self, file):
        # 测一下这个文件是否存在
        try:
            f = open(file, 'rb')
        except:
            print("文件不存在")
            return
        # 防止file带有文件路径，提取文件名
        filename = file.split("/")[-1]
        data = "STOR " + filename
        self.sock.send(data.encode())  # 发请求
        result = self.sock.recv(128).decode()  # 等待回复
        if result == 'OK':
            # 上传文件 读--》发送
            while True:
                data = f.read(1024)
                if not data:
                    break
                self.sock.send(data)
            sleep(0.1)
            self.sock.send(b"##")
            f.close()
        else:
            print("该文件已存在")

    # 处理下载
    def do_get(self, file):
        data = "RETR " + file
        self.sock.send(data.encode())  # 发请求
        result = self.sock.recv(128).decode()  # 等待回复
        if result == 'OK':
            # 接收文件
            f = open(file, 'wb')
            while True:
                data = self.sock.recv(1024)
                if data == b"##":
                    break
                f.write(data)
            f.close()
        else:
            print("该文件不存在")


# 启动函数
def main():
    sock = socket()
    sock.connect(ADDR)

    # 实例化对象用于调用方法
    ftp = FTPClient(sock)

    while True:
        print("""
        ============ 命令选项 =============
                      list 
                    get  file
                    put  file
                      exit
        ==================================
        """)
        cmd = input("请输入命令:")

        if cmd == "list":
            ftp.do_list()
        elif cmd == 'exit':
            ftp.do_exit()
        elif cmd[:3] == 'put':
            file = cmd.split(' ')[-1]
            ftp.do_put(file)
        elif cmd[:3] == 'get':
            file = cmd.split(' ')[-1]
            ftp.do_get(file)
        else:
            print("请输入正确命令")


if __name__ == '__main__':
    main()
