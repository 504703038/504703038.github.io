""" 参数传递 """


def change_1(a: int, b: float, c: str, d: tuple):
    a -= 10
    b -= 10.0
    c = c.replace("Hello", "Hi")
    # d[0] = 5
    pass


def demo_1():
    print("Demo 1:")
    a = 5
    b = 5.0
    c = "Hello World!"
    d = (1, 2, 3, 4)
    change_1(a, b, c, d)
    """ a=5, b=5.0, c=Hello World!, d=(1, 2, 3, 4) """
    print(f"a={a}, b={b}, c={c}, d={d}")
    pass


def change_2(a: list, b: dict):
    a.reverse()
    for key in b.keys():
        b[key] *= 10
    pass


def demo_2():
    print("Demo 2:")
    a = [1, 2, 3, 4]
    b = {"a": 1, "b": 2}
    change_2(a, b)
    """ a=[4, 3, 2, 1], b={'a': 10, 'b': 20} """
    print(f"a={a}, b={b}")
    pass


class MyClass():

    def __init__(self) -> None:
        self.a = 0
        self.b = 0
        pass

    def __str__(self) -> str:
        return f"a={self.a}, b={self.b}"
        pass


def change_3(obj: MyClass):
    obj.a = 10
    obj.b = 20
    pass


def demo_3():
    print("Demo 3:")
    obj = MyClass()
    change_3(obj)
    """ a=10, b=20 """
    print(obj)


if __name__ == "__main__":
    demo_1()
    demo_2()
    demo_3()
    pass
