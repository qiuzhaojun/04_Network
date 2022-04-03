"""
含有参数的进程函数示例
"""
from multiprocessing import Process
from time import sleep

# 含有参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working")

# 位置传参args = ()
# p = Process(target=worker,args=(2,"Levi"))

# 关键字传参 kwargs={}
p = Process(target=worker,
            args=(2,),
            kwargs={"name":"Tom"})

p.start()
p.join(3) # 最多等待3秒

print("==================")
