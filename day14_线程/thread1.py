"""
线程基本使用示例
"""

import threading
from time import sleep
import os

a = 1

# 线程的执行函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放:甜蜜蜜")
    global a
    print("a = ",a)
    a = 10000

# 创建线程对象
t = threading.Thread(target=music)

# 启动线程
t.start()

for i in range(4):
    sleep(1)
    print(os.getpid(),"播放:葫芦娃")

# 回收线程
t.join()

print("a:",a) # ?


