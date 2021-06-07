print('a', 'b', 'c')


def demo(*param):
    print(param)
    print(type(param))


demo(1, 2, 3, 4, 5, 6)


def demo2(param):
    pass


demo2((1, 2, 3, 4, 5, 6))


def demo3(*param):
    pass


a = (1, 2, 3, 4, 5, 6)
demo3(*a)


# 必须参数必须在前面
def demo4(param1, param2=2, *param):
    print(param1)
    print(param2)
    print(param)


demo4('a', 1, 2, 3)
