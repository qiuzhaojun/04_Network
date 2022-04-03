"""
进程属性信息 解释
"""
from multiprocessing import Process
import time

def fun():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)

if __name__ == "__main__":
    # 创建进程对象
    p = Process(target = fun,name="Aid")

    # 该子进程会随父进程而退出 start前设置
    p.daemon = True

    p.start() # 进程有了

    print("Name：",p.name) # 进程名
    print("PID:",p.pid) # PID
    print("is alive:",p.is_alive())

