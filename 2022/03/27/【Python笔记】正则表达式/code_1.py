""" 正则匹配 """
import re
from tool import topic


@topic("Demo-1")
def demo_1():
    string = "www.baidu.com"
    print(re.match("www", string).span())  # 在起始位置匹配
    print(re.match("com", string))  # 不在起始位置匹配
    pass


@topic("Demo-2")
def demo_2():
    string = "www.baidu.com"
    print(re.search("www", string))
    print(re.search("www", string).span())
    print(re.search("com", string))
    print(re.search("com", string).span())

    pattern = re.compile("[abcd]+")
    print(re.search(pattern, string))
    print(re.search(pattern, string).span())
    pass


@topic("Demo-3")
def demo_3():
    string = "www.baidu.com"
    pattern = re.compile("[A-D]+", flags=re.I)
    print(re.findall(pattern, string))

    print(pattern.match(string))
    print(pattern.search(string))
    print(pattern.findall(string))
    pass


if __name__ == "__main__":
    demo_1()
    demo_2()
    demo_3()
    pass
