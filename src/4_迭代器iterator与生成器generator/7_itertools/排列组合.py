from itertools import permutations, combinations, combinations_with_replacement

for p in permutations(['a', 'b', 'c'], 2):
    print(p)
for p in combinations(['a', 'b', 'c'], 2):
    print(p)
# 允许同一个元素被选择多次
for p in combinations_with_replacement(['a', 'b', 'c'], 2):
    print(p)
