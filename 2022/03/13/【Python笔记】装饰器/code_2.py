""" 带参数的装饰器 """


def logging(level):

    def outwrapper(func):

        def wrapper(*args, **kwargs):
            print(f"[{level}]: {func.__name__}() function has been called")
            return func(*args, **kwargs)

        return wrapper

    return outwrapper


@logging(level="INFO")
def hello(a, b, c):
    print(f"a={a}, b={b}, c={c}")
    pass


if __name__ == "__main__":
    hello(1, 2, 3)
    pass
