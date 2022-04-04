""" 闭包 """
from tool import topic


def func_C(c: int):

    def func_D():
        nonlocal c
        c = c**2
        print(f"In func_D, c={c}")

    print(f"In func_C before call func_D, c={c}")
    func_D()
    print(f"In func_C after call func_D, c={c}")
    pass


@topic("Demo-1")
def demo_1():
    func_C(10)
    pass


if __name__ == "__main__":
    demo_1()
    pass
