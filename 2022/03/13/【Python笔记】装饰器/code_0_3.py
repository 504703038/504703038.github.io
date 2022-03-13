""" 函数返回函数 """

from cmath import pi


def function(str="Hello World!!!"):

    def sub_function(str):
        print(f"sub_function: {str}")

    sub_function(str)
    print(str)
    return sub_function


if __name__ == "__main__":
    ret = function()
    ret("sub function test.")
