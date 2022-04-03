"""
Process进程基础创建示例：

将需要新进程执行的事件封装为函数
通过模块的Process类创建进程对象，关联函数
通过进程对象调用start启动进程
通过进程对象调用join回收进程资源
"""
import multiprocessing as mp
from time import sleep

a = 1

# 进程的执行函数
def fun():
    print("开始执行一个进程内容")
    global a
    print("a = ",a)
    a = 10000
    sleep(3)
    print("一个任务假装执行了3秒结束")

def main():
    # 创建进程对象 绑定函数
    p = mp.Process(target=fun)

    # 启动进程  这时进程产生，进程执行fun函数
    p.start()

    print("我也要干点事情")
    sleep(2)
    print("我这件事做了2秒")

    # 阻塞等待回收进程 将创建的进程资源释放
    p.join()

    print("a:",a) # 1

if __name__ == '__main__':
    main()




