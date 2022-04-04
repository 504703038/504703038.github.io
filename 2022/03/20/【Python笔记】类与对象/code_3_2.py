""" 多继承 """
from tool import topic


class A:
    z = 10

    def __init__(self) -> None:
        self.x = 0

        pass

    def func_A(self):
        print("func_A in Class A.")
        return


class B:
    z = 100

    def __init__(self) -> None:
        self.y = 0
        pass

    def func_A(self):
        print("func_A in Class B.")
        return


class C(A, B):

    # def __init__(self) -> None:
    #     super().__init__()

    def func_C(self):
        print(f"x={self.x}")
        # print(f"y={self.y}")
        print(f"z={self.z}")
        pass

    def func_CC(self):
        # print(f"super.x={super().x}")
        # print(f"super.y={super().y}")
        print(f"super.z={super().z}")
        pass


@topic("Demo-1")
def demo_1():
    c = C()

    c.func_A()
    c.func_C()
    c.func_CC()
    pass


class D(A, B):

    def __init__(self) -> None:
        B.__init__(self)

    def func_D(self):
        # print(f"x={self.x}")
        print(f"y={self.y}")
        print(f"z={self.z}")
        pass

    def func_DD(self):
        # print(f"super.x={super().x}")
        # print(f"super.y={super().y}")
        print(f"super.z={super().z}")
        pass

    def func_DDD(self):
        print(f"A.z={A.z}")
        print(f"B.z={B.z}")
        pass


@topic("Demo-2")
def demo_2():
    d = D()
    d.func_D()
    d.func_DD()
    d.func_DDD()
    pass


if __name__ == "__main__":
    demo_1()
    demo_2()
    pass
