""" 函数返回值 """


def return_value_1():
    pass


def demo_1():
    print("Demo 1:")
    ret = return_value_1()
    print(ret)  # None
    pass


def return_value_2(a, b):
    return a + b


def demo_2():
    print("Demo 2:")
    ret = return_value_2(1, 2)
    print(ret)  # 3
    pass


def return_value_3(a, b, c):
    a += 10
    b += 10
    c += 10
    return a, b, c


def demo_3():
    print("Demo 3:")
    ret = return_value_3(1, 2, 3)
    print(ret)  # (11, 12, 13)
    a, b, c = return_value_3(1, 2, 3)
    print(f"a={a}, b={b}, c={c}")  # a=11, b=12, c=13
    # a, b = return_value_3(1, 2, 3)
    # a, b, c, d = return_value_3(1, 2, 3)
    pass


def return_value_4():
    return return_value_2


def demo_4():
    print("Demo 3:")
    add = return_value_4()
    ret = add(1, 2)
    print(ret)  # 3
    pass


if __name__ == "__main__":
    demo_1()
    demo_2()
    demo_3()
    demo_4()
    pass
