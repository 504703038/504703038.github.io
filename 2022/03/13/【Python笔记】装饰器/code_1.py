""" 装饰器 """


def decorator(func):

    def wrap_function():
        print("Before exec func.")
        func()
        print("After exec func.")

    return wrap_function


def need_decoration():
    print("This function need decoration.")


@decorator
def test_function():
    print("In test_function.")
    pass


if __name__ == "__main__":
    my_function = decorator(need_decoration)
    my_function()
    """ output:
        Before exec func.
        This function need decoration.
        After exec func."""


    test_function()
    """ output:
        Before exec func.
        In test_function.
        After exec func. """
    pass