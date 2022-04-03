"""
求100000以内质数之和，写成一个函数
写一个装饰器求一个这个函数运行时间

将100000分成4等份 分别使用4个进程求
每一份的质数之和，四个进程同时执行
记录时间

将100000分成10等份 分别使用10个进程求
每一份的质数之和，10个进程同时执行
记录时间
"""
import time
from multiprocessing import Process

# 装饰器
def timeis(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("函数执行时间：",end_time-start_time)
        return res
    return  wrapper

# 判断一个数n是否为质数
def isprime(n):
    if n <= 1:
        return False
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True

class Prime(Process):
    def __init__(self,begin,end):
        self.begin = begin
        self.end = end
        super().__init__()

    def run(self):
        prime = []
        for i in range(self.begin,self.end):
            if isprime(i):
                prime.append(i) # 是质数加到列表中
        print(sum(prime))


@timeis
def multi_process(n):
    jobs = []
    step = 100000//n
    for i in range(1,100001,step):
        p = Prime(i,i+step)  # 数值区间
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]


# @timeis
# def prime_sum():
#     prime = []
#     for i in range(1,100001):
#         if isprime(i):
#             prime.append(i) # 是质数加到列表中
#     print(sum(prime))

multi_process(20)

# 函数执行时间： 6.944215297698975
# multi_process(10)

# 函数执行时间： 7.557642936706543
# multi_process(4)

# 函数执行时间： 14.412267923355103
# prime_sum()





