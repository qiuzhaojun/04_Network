"""
event 同步互斥方法
"""
from threading import Thread,Event

e = Event() # event对象

msg = None # 用于线程通信

# 线程函数
def 杨子荣():
    print("杨子荣前来拜山头")
    global msg
    msg = "天王盖地虎"
    e.set() # 解除阻塞

if __name__ == "__main__":
    t = Thread(target=杨子荣)
    t.start()

    # 主线程验证口令
    print("说对口令就是自己人")
    e.wait()  # 阻塞等待
    if msg == '天王盖地虎':
        print("宝塔镇河妖")
        print("确认过眼神，你是对的人")
    else:
        print("打死他...无情啊...")

    t.join()

