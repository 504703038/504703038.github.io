""" 触发异常 """
from tool import topic
import traceback


@topic("Demo-1")
def demo_1():
    try:
        raise NameError
    except Exception as e:
        traceback.print_exc()
    pass


@topic("Demo-2")
def demo_2():
    level = 1
    try:
        if level == 1:
            raise Exception("Invalid level!", level)
    except Exception as e:
        traceback.print_exc()
    pass


if __name__ == "__main__":
    demo_1()
    demo_2()
    pass
