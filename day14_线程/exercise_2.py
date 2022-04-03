"""
练习2： 创建两个线程同时执行
一个线程负责打印 1---52   52个数字
另一个线程打印 A--Z  26个字母
要求打印结果为 12A34B.....5152Z
"""

from threading import Thread,Lock

lock1 = Lock()
lock2 = Lock()

def print_num():
    for i in range(1,53,2):
        lock1.acquire()
        print(i)
        print(i + 1)
        lock2.release()

def print_chr():
    for i in range(65,91):
        lock2.acquire()
        print(chr(i))
        lock1.release()

t1 = Thread(target= print_num)
t2 = Thread(target= print_chr)

lock2.acquire() # 让打印数字先执行

t1.start()
t2.start()
t1.join()
t2.join()