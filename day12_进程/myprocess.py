"""
自定义进程类
"""

from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        # 调用父类init保留父类属性
        super().__init__()

    def fun1(self):
        print("假设这个事情很复杂")

    def fun2(self):
        print("特别复杂 too",self.value)

    # 进程做的事情
    def run(self):
        self.fun1()
        self.fun2()

if __name__ == "__main__":
    p = MyProcess(3)
    p.start() # 运行run'作为一个进程
    p.join()
    # 猜想源码怎么写的
    # class Process:
    #     def __init__(self,target=None):
    #         self.target = target
    #
    #     def run(self):
    #         self.target()
    #
    #     def start(self):
    #         self.run()


