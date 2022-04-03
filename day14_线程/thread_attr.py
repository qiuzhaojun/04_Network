"""
线程属性
"""

from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性设置")

t = Thread(target=fun)

# 分之线程会随主线程退出
t.setDaemon(True)

t.start()

print(t.is_alive())
t.setName("Tarena") # 线程名称
print(t.getName())