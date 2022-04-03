from socket import *

# 服务器地址
HOST = "0.0.0.0"
PORT = 8000
ADDR = (HOST,PORT)
user = {}

def login(sock,name,addr):
    if name in user:
        sock.sendto(b'FAIL',addr)
        return
    else:
        sock.sendto(b"OK",addr)
        msg = '欢迎 %s 进入聊天室'%name
        # 循环通知其他人
        for i in user:
            sock.sendto(msg.encode(),user[i])
        user[name] = addr

# 程序启动函数
def main():
    # UDP套接字
    sock = socket(AF_INET,SOCK_DGRAM)
    sock.bind(ADDR)

    #循环接受请求(总分模式)
    while True:
        data,addr = sock.recvfrom(1024)
        tmp = data.decode().split(' ')
        print(data,addr)
        if tmp[0] == "LOGIN":
            login(sock,tmp[1],addr)

        elif tmp[0] == "CHAT":
            pass
        elif tmp[0] == "EXIT":
            pass

if __name__ == '__main__':
    main()
