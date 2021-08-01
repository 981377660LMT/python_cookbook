items = [1, 2, 3]
it = iter(items)

print(next(it, None))
print(next(it, None))
print(next(it, None))
# 不加这个default参数会抛出错误
print(next(it, None))
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
