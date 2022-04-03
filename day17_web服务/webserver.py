"""
web server 程序

完成一个类，提供给使用者
可以通过这个类快速搭建服务
完成网页展示
"""
from socket import *
from select import select
import re

# 封装所有web后端功能
class WebServer:
    def __init__(self, host="0.0.0.0", port=80, html=None):
        self.host = host
        self.port = port
        self.html = html
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.create_socket()
        self.bind()

    # 创建设置套接字
    def create_socket(self):
        self.sock = socket()
        self.sock.setblocking(False)

    # 绑定地址
    def bind(self):
        self.address = (self.host, self.port)
        self.sock.bind(self.address)

    # 启动整个服务
    def start(self):
        self.sock.listen(5)
        print("Listen the port %d" % self.port)
        # 先监控监听套接字
        self.rlist.append(self.sock)
        # 循环监控IO对象
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            # 处理就绪的IO
            for r in rs:
                # 有客户端连接
                if r is self.sock:
                    connfd, addr = r.accept()
                    print("Connect from", addr)
                    # 将客户端连接套接字也监控起来
                    connfd.setblocking(False)
                    self.rlist.append(connfd)
                else:
                    # 处理浏览器端发的请求
                    try:
                        self.handle(r)
                    except:
                        pass
                    self.rlist.remove(r)
                    r.close()

    # 处理客户端请求
    def handle(self, connfd):
        # http请求
        request = connfd.recv(1024 * 10).decode()
        # 使用正则匹配请求内容
        pattern = r"[A-Z]+\s+(?P<info>/\S*)"
        result = re.match(pattern, request)
        if request:
            # 提取请求内容
            info = result.group("info")
            print("请求内容:",info)
            self.send_html(connfd,info)

    # 发送响应
    def send_html(self,connfd,info):
        # 对info分情况
        if info == "/":
            filename = self.html + "/index.html"
        else:
            filename = self.html + info

        # 打开判断文件是否存在
        try:
            file = open(filename,"rb")
        except:
            #　请求的网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            with open(self.html+"/404.html") as file:
                response += file.read()
            response = response.encode()
        else:
            # 请求的网页存在
            data = file.read() #　字节串
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "Content-Length:%d\r\n"%len(data)
            response += "\r\n"
            response = response.encode() + data
            file.close()
        finally:
            connfd.send(response)



if __name__ == '__main__':
    # 需要用户决定： 地址  网页
    httpd = WebServer(host="0.0.0.0",
                      port=8000,
                      html="./static")
    # 启动服务
    httpd.start()
