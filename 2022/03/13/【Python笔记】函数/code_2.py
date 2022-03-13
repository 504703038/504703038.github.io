""" 参数 """


def add(a, b):
    return a + b


def demo_1():
    print("Demo 1:")
    print(add(1, 2))


def sum_abcd(a, b, c=0, d=0):
    return a + b + c + d


def demo_2():
    print("Demo 2:")
    print(sum_abcd(1, 2, 3, 4))
    print(sum_abcd(1, 2, c=3, d=4))
    print(sum_abcd(1, 2, d=4))
    print(sum_abcd(1, d=4, b=2))
    # print(sum_abcd(1, c=3, d=4))
    pass


def max(*args):
    print(type(args))  # tuple
    print(args)
    num = len(args)
    if num == 0:
        return None
    ret = args[0]
    for item in args:
        if item > ret:
            ret = item
    return ret


def demo_3():
    print("Demo 3:")
    print(max())
    print(max(1, 2, 3, 4, 5, 6))
    arr = (1, 2, 3, 4, 5, 6)
    print(max(*arr))
    arr = [1, 2, 3, 4, 5, 6]
    print(max(*arr))


def print_dict(**args):
    print(type(args))  # dict
    print(args)
    num = len(args)
    if num == 0:
        print(None)
    for key, value in args.items():
        print(f"{key} = {value}")
    pass


def demo_4():
    print("Demo 4:")
    print_dict()
    print_dict(a=1, b=2, c=3, d=4)
    dic = {"a": 1, "b": 2, "c": 3, "d": 4}
    print_dict(**dic)
    print(sum_abcd(**dic))


def test_var_args(a, b, *args, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(args)
    print(kwargs)
    pass


def demo_5():
    print("Demo 5:")
    test_var_args(1, 2, 3, 4, e=5, f=6)
    test_var_args(1, 2, 3, 4)
    test_var_args(1, 2, e=5, f=6)
    pass


if __name__ == "__main__":
    demo_1()
    demo_2()
    demo_3()
    demo_4()
    demo_5()
    pass
