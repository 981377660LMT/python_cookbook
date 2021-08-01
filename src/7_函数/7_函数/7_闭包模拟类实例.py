# 这个案例中，闭包的方案运行起来要快大概8%，
# 大部分原因是因为对实例变量的简化访问，
# 闭包更快是因为不会涉及到额外的self变量。
import sys
from timeit import timeit


class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # Update instance dictionary with callables
        self.__dict__.update((key, value) for key, value in locals.items() if callable(value))

    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()


# Example use
def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


s = Stack()
print(len(s))
s.push(10)
print(s)

# 有趣的是，这个代码运行起来会比一个普通的类定义要快很多
print(timeit('s.push(1);s.pop()', 'from __main__ import s'))

# 在配置的时候给闭包添加方法会有更多的实用功能，
# 比如你需要重置内部状态、刷新缓冲区、清除缓存或其他的反馈机制的时候。