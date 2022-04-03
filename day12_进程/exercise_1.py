"""
练习1 ： 大文件拆分
将一个文件拆分成2个部分，按照字节数平分
要求使用两个子进程完成这件事，要求上下两个部分
的拆分工作同时进程

思路： 一个进程拷贝上半部分  函数
      一个进程拷贝下半部分  函数
      两个子进程同时执行
      os.path.getsize() 获取文件大小
      文件操作位置: seek(1000,0)
"""
from multiprocessing import Process
import os

# 获取文件大小
size = os.path.getsize("zly.jpg")

# 如果父进程中打开文件，各子进程直接使用fr
# 那么文件偏移量会相互影响，所以这里应该在各自子
# 进程中打开
# fr = open("zly.jpg", 'rb')

# 上半部分
def top():
    fr = open("zly.jpg", 'rb')
    fw = open("top.jpg", 'wb')
    n = size // 2 # 从头开始复制n个字节
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    else:
        fw.write(fr.read(n))
    fr.close()
    fw.close()

# 下半部分
def bot():
    fr = open("zly.jpg",'rb')
    fw = open("bot.jpg",'wb')
    fr.seek(size//2,0) # 偏移量放在中间
    while True:
        # 从一半开始复制
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

if __name__ =='__main__':
    jobs = [] # 存储进程对象
    # 循环创建进程
    for th in [bot,top]:
       p = Process(target=th)
       jobs.append(p) # 存储进程对象
       p.start()

    [i.join() for i in jobs]