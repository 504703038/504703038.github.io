""" 自定义元类 """
from tool import topic


def my_meta_class(class_name, class_parents, class_attr):
    """ 自定义元类
    将类中非"__"开头的属性改为大写
    """
    new_attr = {}
    for name, value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value
        pass
    return type(class_name, class_parents, new_attr)


class A(object, metaclass=my_meta_class):
    a = 1

    def func_A(self):
        pass

    pass


@topic("Demo-1")
def demo_1():
    a = A()
    print(type(A))
    print(A.__dict__)
    pass


class MyMetaClass(type):

    def __new__(cls, class_name, class_parents, class_attr):
        new_attr = {}
        for name, value in class_attr.items():
            if not name.startswith("__"):
                new_attr[name.upper()] = value
            pass
        return type(class_name, class_parents, new_attr)


class B(metaclass=MyMetaClass):
    b = 1

    def func_B(self):
        pass

    pass


@topic("Demo-2")
def demo_2():
    a = B()
    print(type(B))
    print(B.__dict__)
    pass


if __name__ == "__main__":
    demo_1()
    demo_2()
    pass
