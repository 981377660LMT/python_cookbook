from collections import Iterable

# ignore_types用来将字符串和字节排除在可迭代对象外，防止将它们再展开成单个的字符。
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8, 'as']
# Produces 1 2 3 4 5 6 7 8
for x in flatten(items):
    print(x)
