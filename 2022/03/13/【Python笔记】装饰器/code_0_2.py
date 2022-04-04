""" 在函数中定义函数 """


def function(str="Hello World!!!"):

    def sub_function(str):
        print(f"sub_function: {str}")

    sub_function(str)
    print(str)


if __name__ == "__main__":
    function()
    try:
        sub_function()
    except NameError:
        print("There is no function named \"sub_function\"")
    pass
