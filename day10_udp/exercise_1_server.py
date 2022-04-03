"""
练习： 编写一个服务端和一个客户端
客户端循环输入单词，发送给服务端，从服务端获取
单词解释，打印出来。

* 使用 dict --> words 表完成
* 数据库和服务端一定是在一起的
"""

from socket import *
import pymysql

# 连接数据库的字典
DATABASE = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"dict",
    "charset":"utf8"
}

# 服务器地址
ADDR = ("0.0.0.0",8888)

# 数据处理
class Database:
    def __init__(self):
        self.db = pymysql.connect(**DATABASE)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    # 查找单词
    def query_word(self,word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql,[word])
        mean = self.cur.fetchone() # 得到解释 （）
        # 考虑是否查询到
        if mean:
            return mean[0]
        else:
            return "Not Found"


def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(ADDR)
    db = Database() # 实例化对象，处理数据库方法

    # 接收单词
    while True:
        word,addr = udp_socket.recvfrom(50)
        # 查找单词解释
        mean = db.query_word(word.decode())
        # 发送单词解释
        udp_socket.sendto(mean.encode(),addr)

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()



