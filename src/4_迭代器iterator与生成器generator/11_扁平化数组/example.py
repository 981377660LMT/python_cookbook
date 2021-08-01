# Example of flattening a nested sequence using subgenerators

from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        # 字符串和字节的额外检查是为了防止将它们再展开成单个字符
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            # 相当于
            # for i in flatten(x):
            #     yield i
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]

# Produces 1 2 3 4 5 6 7 8
for x in flatten(items):
    print(x)

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)
