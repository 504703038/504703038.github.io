""" 一切皆对象 """


def hello(str="Hello World!!!"):
    print(str)



if __name__ == "__main__":
    hello()
    greet = hello
    greet()
    
    del hello
    try:
        hello()
    except NameError:
        print("There is no function named \"hello\"")
    
    greet()
    pass
