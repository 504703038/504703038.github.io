""" LEGB规则 """


def demo_1():
    tmp = 10
    print(tmp)  # 局部变量


def sq(x):
    print(f"Global function sq, x={x}")
    pass


def demo_2(a):

    def sq(x):
        return x**a  # 嵌套作用域

    return sq(2)


def demo_3():
    print(total)  # 全局变量


def demo_4():
    print(__name__)  # 内置作用域


if __name__ == "__main__":
    demo_1()

    ret = demo_2(10)
    print(ret)

    total = 100
    demo_3()

    demo_4()
    pass
