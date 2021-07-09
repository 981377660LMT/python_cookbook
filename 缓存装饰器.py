# -*- coding: utf-8 -*-
import functools


def cache(func):
    store = {}

    @functools.wraps(func)
    def wrapper(n):  # wrapper是一个闭包函数
        if n in store:
            return store[n]
        else:
            res = func(n)
            store[n] = res
            return res

    return wrapper


@cache
# 尾递归就是把当前的运算结果（或路径）放在参数里传给下层函数
def f(n):
    if n <= 1:
        return 1
    return f(n - 1) + f(n - 2)


print(f(100))

