# Examples of different ways to filter data

from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# All positive values
# 使用列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结果集，占用大量内存
#  如果你对内存比较敏感，那么你可以使用生成器表达式迭代产生过滤的元素
pos = (n for n in mylist if n > 0)
print(pos)

# All negative values
neg = [n for n in mylist if n < 0]
print(neg)

# Negative values clipped to 0
neg_clip = [n if n > 0 else 0 for n in mylist]
print(neg_clip)

# Positive values clipped to 0
pos_clip = [n if n < 0 else 0 for n in mylist]
print(pos_clip)

# Compressing example

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]
# 过滤规则比较复杂

# 这里的关键点在于先创建一个 Boolean 序列，指示哪些元素符合条件。
#  然后 compress() 函数根据这个序列去选择输出对应位置为 True 的元素。
# 和 filter() 函数类似， compress() 也是返回的一个迭代器。
# 因此，如果你需要得到一个列表， 那么你需要使用 list() 来将结果转换为列表类型。
more5 = [n > 5 for n in counts]
# [False, False, True, False, False, True, True, False]
a = list(compress(addresses, more5))
print(a)
