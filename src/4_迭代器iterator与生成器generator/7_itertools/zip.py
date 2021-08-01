from itertools import zip_longest

a = [1, 2, 3]
b = ['a', 'b', 'c', 'd']
for i in zip_longest(a, b, fillvalue=666):
    print(i)

