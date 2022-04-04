""" 异常处理 """
from tool import topic


@topic("Demo-1")
def demo_1():
    print(x)
    pass


@topic("Demo-2")
def demo_2():
    try:
        print(5 / 0)
    except (NameError, IOError):
        print("There is a NameError or IOError occured.")
    pass


@topic("Demo-3")
def demo_3():
    try:
        print(x)
    except:
        print("Name Error occured.")
        return
    finally:
        print("demo_3 end.")
    print("In function demo_3.")
    pass


if __name__ == "__main__":
    demo_1()
    demo_2()
    demo_3()
    pass
