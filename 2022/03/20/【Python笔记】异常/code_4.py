""" 自定义异常 """
from tool import topic
import traceback


class MyException(Exception):

    def __init__(self, name, reason):
        self.name = name
        self.reason = reason


@topic("Demo-1")
def demo_1():
    try:
        raise MyException("TimeoutError", "Connection timeout.")
    except MyException as e:
        print(f"{e.name}: {e.reason}")
    pass


if __name__ == "__main__":
    demo_1()
    pass
