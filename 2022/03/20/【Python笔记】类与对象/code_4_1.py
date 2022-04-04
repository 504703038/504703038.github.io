""" 元类 
MyClass = MetaClass()
my_object = MyClass() 
"""
from tool import topic


class A:
    a = 10

    def func_A():
        print("In Class A.")


class B:
    b = 100

    def func_B():
        print("In Class B.")


class C(A, B):
    c = 1000

    def func_C(self):
        print("In Class C.")

    @staticmethod
    def static_method(str):
        print(f"In C.static_method, str='{str}'.")
        pass

    @classmethod
    def class_method(cls):
        print(f"In C.class_method, c={cls.c}.")
        pass


def func_C(self):
    print("In global function func_C.")
    pass


@staticmethod
def static_method(str):
    print(f"In global function static_method, str='{str}'.")
    pass


@classmethod
def class_method(cls):
    print(f"In global function class_method, c={cls.c}.")
    pass


@topic("Demo-1")
def demo_1():
    c = C()
    c.func_C()
    c.static_method("Hello.")
    c.class_method()
    pass


@topic("Demo-2")
def demo_2():
    C = type(
        "C", (A, B), {
            "c": 1000,
            "func_C": func_C,
            "static_method": static_method,
            "class_method": class_method
        })

    c = C()
    c.func_C()
    c.static_method("Hello.")
    c.class_method()
    pass


if __name__ == "__main__":
    demo_1()
    demo_2()
    pass
