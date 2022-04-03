def login():
    # 二级界面
    while True:
        print("""
        ============ 查询界面 ==============
         1. 查单词   2. 历史记录   3. 注销
        ===================================
            """)
        cmd = input("请输入命令:")

        if cmd == "1":
            pass
        elif cmd == '2':
            pass
        elif cmd == '3':
            break  # 退出二级界面
        else:
            print("请输入正确命令")

# 一级界面
while True:
    print("""
    ============ 登录界面 =============
      1. 注册     2. 登录     3. 退出
    ==================================
    """)
    cmd = input("请输入命令:")

    if cmd == "1":
        pass
    elif cmd == '2':
        login() # 调用二级界面函数
    elif cmd == '3':
        break # 退出一级界面
    else:
        print("请输入正确命令")

