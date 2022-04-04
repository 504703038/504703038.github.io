""" 类做装饰器 """


class DebugLogging(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"[DEBUG]: {self.func.__name__}() function has been called")
        return self.func(*args, **kwargs)


@DebugLogging
def func_A(a, b, c):
    print(f"a={a}, b={b}, c={c}")
    pass


class Logging(object):

    def __init__(self, level):
        self.level = level
        pass

    def __call__(self, func):

        def wrapper(*args, **kwargs):
            print(
                f"[{self.level}]: {func.__name__}() function has been called")
            return func(*args, **kwargs)

        return wrapper


@Logging("INFO")
def func_B(a, b, c):
    print(f"a={a}, b={b}, c={c}")
    pass


if __name__ == "__main__":
    func_A(1, 2, 3)
    print("*" * 20)
    func_B(4, 5, 6)
    pass
