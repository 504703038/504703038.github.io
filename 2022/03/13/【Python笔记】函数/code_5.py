""" lambda函数 """


def demo_1():
    print("Demo 1:")
    sq = lambda x: x**2
    ret = sq(10)
    print(ret)  # 100
    pass


def demo_2():
    print("Demo 2:")
    """ lambda [arg1 [,arg2,.....argn]]:expr1 if condition else expr2 """
    max = lambda x, y: x if x > y else y
    ret = max(10, 100)
    print(ret)  #100
    pass


if __name__ == "__main__":
    demo_1()
    demo_2()
    pass
