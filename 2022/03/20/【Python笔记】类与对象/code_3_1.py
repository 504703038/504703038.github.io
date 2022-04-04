""" 继承 """
from tool import topic


class A:
    y = 100

    def __init__(self) -> None:
        self.x = 10
        pass

    def func_A(self):
        print("func_A in Class A.")
        return


class B(A):
    pass


class C(A):

    # def __init__(self) -> None:
    #     super().__init__()

    def func_A(self):
        print("func_A in Class C.")


@topic("Demo-1")
def demo_1():
    a = A()
    b = B()
    c = C()

    a.func_A()
    b.func_A()
    c.func_A()
    pass


@topic("Demo-2")
def demo_2():
    a = A()
    b = B()
    c = C()

    print(c.x)
    print(c.y)
    pass


if __name__ == "__main__":
    demo_1()
    demo_2()
    pass
