""" 全局边变量与局部变量 """

# total = 0  # 全局变量


def demo_1():
    total = 100  # 局部变量
    pass


def demo_2(total):
    total = 100
    pass


def demo_3():
    global total
    total = 100  # 全局变量
    pass


def demo_4(total):
    # global total  # "total" is assigned before global declaration
    total = 100
    pass


def demo_5():
    global g_total
    g_total = 100
    pass


if __name__ == "__main__":
    total = 0
    demo_1()
    print(total)  # 全局变量total: 0

    total = 0
    demo_2(total)
    print(total)  # 全局变量total: 0

    total = 0
    demo_3()
    print(total)  # 全局变量total: 100

    demo_5()
    print(g_total)  # 全局变量g_total: 100
    pass
