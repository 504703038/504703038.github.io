""" 闭包 """
from tool import topic


def nth_power(exponent):
    """ 闭包可以避免使用全局值，并提供某种形式的数据隐藏。 """

    def exponent_of(base):
        return base**exponent

    return exponent_of


@topic("Demo-1")
def demo_1():
    sqr = nth_power(2)
    cube = nth_power(3)
    print(f"sqr(5)={sqr(5)}")
    print(f"cube(5)={cube(5)}")

    print(sqr.__closure__)
    print(sqr.__closure__[0].cell_contents)
    print(cube.__closure__[0].cell_contents)
    pass


if __name__ == "__main__":
    demo_1()
    pass
