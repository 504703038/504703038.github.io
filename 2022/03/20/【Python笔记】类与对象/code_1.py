""" 类的定义与实例化 """
from ast import Mult
from tool import topic


class MyClass:
    """ 自定义类 """
    x = 10

    def __init__(self) -> None:
        self.y = 0
        pass

    def func(abcd) -> str:
        return f"x={abcd.x}, y={abcd.y}"

    @staticmethod
    def static_method(str):
        # print(f"In MyClass.static_method, x={x}")
        print(f"In MyClass.static_method, str='{str}'")
        pass

    @classmethod
    def class_method(cls):
        print(f"In MyClass.static_method, x={cls.x}")
        pass


@topic("Demo-1")
def demo_1():
    """ 类的类型 """
    print(MyClass)
    print(type(MyClass))
    pass


@topic("Demo-2")
def demo_2():
    """ 类成员变量与方法的调用 """
    obj = MyClass()
    print(MyClass.x)
    # print(MyClass.func())
    MyClass.static_method("Class Call")
    MyClass.class_method()

    print(f"x={obj.x}")
    print(obj.func())
    obj.static_method("Object Call")
    obj.class_method()


    # 新增成员变量
    obj.z = 100
    print(f"obj.z={obj.z}")
    MyClass.v = 1000
    print(f"obj.v={obj.v}")
    print(f"MyClass.v={MyClass.v}")
    pass


@topic("Demo-3")
def demo_3():
    """ 删除成员变量与函数 """
    obj = MyClass()
    del MyClass.x
    del obj.y
    # print(obj.x)
    # print(obj.y)
    del MyClass.func
    # del obj.func
    # print(obj.func())
    pass


if __name__ == "__main__":
    demo_1()
    demo_2()
    demo_3()
    pass