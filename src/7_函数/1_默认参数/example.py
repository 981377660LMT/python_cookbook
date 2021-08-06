# Examples of a function with default arguments

# (a) Dangers of using a mutable default argument

# 默认参数的值仅仅在函数定义的时候赋值一次 与js不同js是调用时赋值
# 默认参数的值应该是不可变的对象，比如None、True、False、数字或字符串
def spam1(b=[]):
    return b


a = spam1()
print(a)
a.append(1)
a.append(2)
b = spam1()
print(b)  #  Carefully observe result
print('-' * 10)

# (b) Better alternative for mutable defaults
def spam2(b=None):
    if b is None:
        b = []
    return b


a = spam2()
print(a)
a.append(1)
a.append(2)
b = spam2()
print(b)
print('-' * 10)

# (c) Example of testing if an argument was supplied or not

# 一个函数需要测试某个可选参数是否被使用者传递进来
# js 中可以使用symbol
_no_value = object()
# object()唯一能做的就是测试同一性
def spam3(b=_no_value):
    if b is _no_value:
        print("No b value supplied")
    else:
        print("b=", b)


spam3()
spam3(None)
spam3(0)
spam3([])
