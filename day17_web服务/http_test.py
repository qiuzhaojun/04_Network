"""
http 请求响应示例
"""
from socket import *

s = socket()
s.bind(("0.0.0.0",8888))
s.listen(5)

c,addr = s.accept() # 浏览器连接
print("Connect from",addr)

# 接收浏览器发送的HTTP请求
data = c.recv(1024 * 10)
print(data.decode())

# 发送http响应给浏览器
response = "HTTP/1.1 404 Not Found\r\n"
response += "Content-Type:text/html\r\n"
response += "\r\n"
response += "Sorry...."

c.send(response.encode())

c.close()
s.close()

