# 装饰器，类似Java的注解
import time


def f1():
    print('This is a function1')


def f2():
    print('This is a function2')


# unix 时间戳，从1970-01-01 00:00:00开始的秒数
f1()


# 对修改是封闭的，对扩展是开放的
def print_current_time(func):
    print(time.time())
    func()


print_current_time(f1)
print_current_time(f2)
