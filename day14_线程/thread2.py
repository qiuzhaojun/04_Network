"""
创建线程实例2
"""
from threading import Thread
from time import sleep

# 含有参数的线程函数
def fun(sec,name):
    print("含有参数的线程函数")
    sleep(sec)
    print("%s线程执行完成"%name)

# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=fun,
               args=(2,),
               kwargs={"name":"T%d"%i})
    jobs.append(t)
    t.start() # 启动线程

# 回收线程
[i.join() for i in jobs]