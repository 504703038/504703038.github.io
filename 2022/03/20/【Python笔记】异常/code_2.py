""" 打印异常信息 """
from tool import topic
import traceback


@topic("Demo-1")
def demo_1():
    try:
        print(5 / 0)
    except Exception as e:
        print(e)
    pass


@topic("Demo-2")
def demo_2():
    try:
        print(5 / 0)
    except Exception as e:
        traceback.print_exc()
    pass


if __name__ == "__main__":
    demo_1()
    demo_2()
    pass
