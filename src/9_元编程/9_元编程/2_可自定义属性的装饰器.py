# 引入一个访问函数，使用 nonlocal 来修改内部变量。 然后这个访问函数被作为一个属性赋值给包装函数。

import time
from functools import partial, wraps


def attach_wrapper(attach_target):
    def decorator(func):
        setattr(attach_target, func.__name__, func)

    return decorator


def bar(state: int):
    def timethis(func):
        """
        Decorator that reports the execution time.
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(func.__name__, end - start, state)
            return result

        @attach_wrapper(wrapper)
        def set_state(value: int):
            nonlocal state
            state = value

        return wrapper

    return timethis


@bar(5)
def foo():
    print(666)


foo()

foo.set_state(2)

foo()