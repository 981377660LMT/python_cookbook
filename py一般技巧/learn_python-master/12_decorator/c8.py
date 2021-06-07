import time


# 装饰
def decorator(func):
    # 被封装
    # args是可变参数
    # kwargs是关键字参数
    def wrapper(*args, **kwargs):
        print(time.time())
        # 这种方式最抽象的函数调用方式，适用于任何情况
        func(*args, **kwargs)

    return wrapper


# 装饰器语法糖
@decorator
def f1(func_name):
    print("This is function named " + func_name)


@decorator
def f2(func_name1, func_name2):
    print("This is function named " + func_name1)
    print("This is function named " + func_name2)


@decorator
def f3(func_name1, func_name2, **kwargs):
    print("This is function named " + func_name1)
    print("This is function named " + func_name2)
    print(kwargs)


# f = decorator(f1)
# f()

f1('abc')
f2('hello', 'world')
f3('t1', 't2', a=1, b=2, c='123')
