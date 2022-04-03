"""
消息队列进程间通信演示
"""
from multiprocessing import Process,Queue

# 创建消息队列
q = Queue()

def request():
    name = "Levi"
    passwd = "123456"
    # 通过消息队列传送给另外一个进程
    q.put(name)
    q.put(passwd)

def handle():
    # 从消息队列获取内容
    name = q.get()
    passwd = q.get()
    print("用户:",name)
    print("密码:",passwd)

p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()