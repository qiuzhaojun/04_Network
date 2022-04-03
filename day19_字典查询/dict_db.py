"""
dict
数据处理模块
"""
import pymysql
import hashlib

# 连接数据库的字典
DATABASE = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"dict",
    "charset":"utf8"
}

# cookie 扩展
def change_passwd(passwd):
    hash = hashlib.md5() # 加密算法对象
    hash.update(passwd.encode()) # 加密处理
    return hash.hexdigest() # 获取加密后的结果


# 数据处理
class Database:
    def __init__(self):
        self.db = pymysql.connect(**DATABASE)

    def create_cursor(self):
        self.cur = self.db.cursor()

    def close(self):
        self.db.close()

    def register(self,name,passwd):
        sql = "select name from user where name=%s;"
        self.cur.execute(sql,[name])
        # 如果查询到则该用户存在
        if self.cur.fetchone():
            return False

        # 插入用户
        passwd = change_passwd(passwd)
        sql = "insert into user (name,passwd) values (%s,%s);"
        try:
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    # 处理登录
    def login(self, name, passwd):
        passwd = change_passwd(passwd) # 获取加密后的密码
        # binary 查询区分字母大小写
        sql = "select name from user where binary name=%s and binary passwd=%s;"
        self.cur.execute(sql, [name,passwd])
        # 如果查询到该用户则可以登录
        if self.cur.fetchone():
            return True
        else:
            return False

    # 查询单词
    def query(self,word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql,[word])
        result = self.cur.fetchone() # (mean,) or None
        if result:
            return result[0]
        else:
            return "Not Found"

    # 插入历史记录
    def insert_history(self,name,word):
        # history-> id  word  time  user_id
        sql = "insert into history (word,user_id) values (%s,(select id from user where name=%s));"
        try:
            self.cur.execute(sql,[word,name])
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    # 查询历史记录
    def history(self,name):
        # name word time
        sql = "select name,word,time " \
              "from user inner join history " \
              "on user.id=history.user_id " \
              "where name = %s " \
              "order by time desc " \
              "limit 10;"
        self.cur.execute(sql,[name])
        # ((name,word,time),()....)
        return self.cur.fetchall()
