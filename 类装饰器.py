# -*- coding: utf-8 -*-
import functools


class Memo:
    def __init__(self, state: int) -> None:
        self.state = state

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(self.state)
            return func(*args, **kwargs)

        return wrapper


@Memo(5)
def foo():
    ...


foo()

