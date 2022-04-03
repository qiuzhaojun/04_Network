"""
进程池使用示例

* 父进程退出则进程池会自动销毁
"""
from multiprocessing import Pool
from time import sleep,ctime
import random

# 进程池事件函数
def worker(msg,sec):
    print(ctime(),"---",msg)
    sleep(sec)

# 创建进程池
pool = Pool(4)

# 向进程池队列添加事件
for i in range(10):
    msg = "Tedu-%d"%i
    pool.apply_async(func=worker,
                     args=(msg,random.randint(1,4)))

# 关闭进程池  不能添加新的事件
pool.close()

# 阻塞回收进程池
pool.join()
