# Iterating over merged sorted iterables

import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
# heapq.merge 可迭代特性意味着它不会立马读取所有序列
for c in heapq.merge(a, b):
    print(c)

