"""
练习：模拟一个售票系统程序
一共500张票 ---》T1---T500

编程10个线程模拟10个售票窗口机器 记为 W1-W10
10个窗口同时售票知道所有票都卖出为止

票按照顺序出售
每个窗口卖出一张后   w2----T346
卖出一张需要0.1s
"""

from threading import Thread
from time import sleep

ticket = ["T%d" % x for x in range(1,501)]

# 买票函数
def sell(w):
    while ticket:
        print("%s --- %s"%(w,ticket.pop(0)))
        sleep(0.1)

jobs = []
for i in range(1,11):
    t = Thread(target=sell,args=("w%d"%i,))
    jobs.append(t)
    t.start() # 启动线程

# 回收线程
[i.join() for i in jobs]