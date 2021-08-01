# example.py
# 命名元组的一个主要用途是将你的代码从下标操作中解脱出来
from collections import namedtuple

# nametuple源码的返回值为
#  result = type(typename, (tuple,), class_namespace)
# 即返回了一个父类为tuple的类
Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


# Some Data
records = [('GOOG', 100, 490.1), ('ACME', 100, 123.45), ('IBM', 50, 91.15)]

print(compute_cost(records))

