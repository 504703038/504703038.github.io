""" 类的内置函数与重载 """
from tool import topic


class MyClass:
    """ 自定义类 """

    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        pass


class AnotherClass:
    """ 另一个自定义类 """

    def __init__(self) -> None:
        self.val = 0
        pass

    def __str__(self) -> str:
        return f"val={self.val}"

    def __eq__(self, __o: object) -> bool:
        return self.val == __o.val

    def __ne__(self, __o: object) -> bool:
        return self.val != __o.val

    def __le__(self, __o: object) -> bool:
        return self.val <= __o.val

    def __ge__(self, __o: object) -> bool:
        return self.val >= __o.val

    def __lt__(self, __o: object) -> bool:
        return self.val < __o.val

    def __gt__(self, __o: object) -> bool:
        return self.val > __o.val


@topic("Demo-1")
def demo_1():
    """ 类的内置变量与函数 """
    obj = MyClass()
    other_obj = MyClass()
    print(dir(obj))

    # 内置变量
    print(obj.__dict__)
    print(obj.__doc__)

    # 内置函数
    # obj.__init__()
    # obj.__str__()
    # obj.__eq__(other_obj)
    # obj.__ne__(other_obj)
    # obj.__le__(other_obj)
    # obj.__ge__(other_obj)
    # obj.__lt__(other_obj)
    # obj.__gt__(other_obj)

    pass


@topic("Demo-2")
def demo_2():
    """ 类的函数重载 """
    obj1 = AnotherClass()
    obj2 = AnotherClass()

    print(obj1)

    obj1.val = 1
    obj2.val = 1
    print(obj1 == obj2)
    print(obj1 != obj2)
    print(obj1 >= obj2)
    print(obj1 <= obj2)
    print(obj1 > obj2)
    print(obj1 < obj2)
    pass


if __name__ == "__main__":
    demo_1()
    demo_2()
    pass