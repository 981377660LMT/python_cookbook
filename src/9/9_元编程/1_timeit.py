import time
from functools import wraps
from inspect import signature


def timethis(func):
    """
    Decorator that reports the execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def foo(x: int):
    print(x)


foo(1)
print(foo.__annotations__)
print(signature(foo))
# 假设装饰器是通过 @wraps (参考9.2小节)来实现的，那么你可以通过访问 __wrapped__ 属性来访问原始函数：
print(foo.__wrapped__)