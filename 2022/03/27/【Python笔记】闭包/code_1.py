""" 闭包 """
from tool import topic


def func_A(a: int):

    def func_B(b: int):
        return a + b

    return func_B


@topic("Demo-1")
def demo_1():
    my_func = func_A(5)
    ret = my_func(10)
    print(f"ret={ret}")
    pass


if __name__ == "__main__":
    demo_1()
    pass
