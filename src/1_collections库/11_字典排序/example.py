# example.py
#
# Sort a list of a dicts on a common key
# 通过某个关键字排序一个字典列表
from pprint import pprint
from operator import itemgetter


rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
]


rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))


print("Sorted by fname:")
pprint(rows_by_fname)

print("Sorted by uid:")
pprint(rows_by_uid)

# 如果使用list表示多个键，则会有TypeError: 'list' object is not callable的问题
# 此时itemgetter内部的__call__调用函数
# def func(obj):
#     return tuple(obj[i] for i in items)
# itemgetter() 函数就是负责创建这个 callable 对象的。

# rows_by_lfname = sorted(rows, key=('lname', 'fname'))
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print("Sorted by lname,fname:")
pprint(rows_by_lfname)

# sort/max/min的key都需要Callable
