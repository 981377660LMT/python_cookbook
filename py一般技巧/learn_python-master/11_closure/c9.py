def a():
    pass


print(type(a))


# 闭包 = 函数 + 环境变量（函数定义时候）
# 现场
def curve_pre():
    # a必须是局部变量
    a = 25

    def curve(x):
        return a * x * x
    return curve


def curve_pre1():
    # a必须是局部变量
    a = 30

    def curve(x):
        return a * x * x
    return curve


a = 10
f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(2))
