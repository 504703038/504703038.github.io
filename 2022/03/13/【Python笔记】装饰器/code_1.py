""" 装饰器 """

from functools import wraps


def decorator(func):
    """ @wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。
    这可以让我们在装饰器里面访问在装饰之前的函数的属性。 """

    # @wraps(func)
    def wrap_function():
        print("Before exec func.")
        return func()

    return wrap_function


@decorator
def test_function():
    print("In test_function.")
    pass


if __name__ == "__main__":
    test_function()
    print("*" * 20)
    print(test_function.__name__)
    pass