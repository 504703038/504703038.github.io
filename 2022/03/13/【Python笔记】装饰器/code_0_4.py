""" 函数作为参数传递 """


def function(str="Hello World!!!"):

    def sub_function(str):
        print(f"sub_function: {str}")

    sub_function(str)
    print(str)
    return sub_function


def test_function(func):
    func("Call func, in test_function.")
    pass


if __name__ == "__main__":
    ret = function()
    test_function(ret)
