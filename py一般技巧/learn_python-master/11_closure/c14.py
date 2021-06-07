def f1():
    a = 10

    def f2():
        # a此时将被理解为一个局部变量
        # a = 20
        print(a)
    print(a)
    f2()
    print(a)
    return f2


f = f1()
print(type(f))
print(f.__closure__)
