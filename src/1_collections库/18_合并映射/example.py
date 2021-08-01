# example.py
#
# Example of combining dicts into a chainmap
# (a) Simple example of combining
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# ChainMap 使用原来的字典，它自己不创建新的字典
# ChainMap 类只是在内部创建了一个容纳这些字典的列表 并重新定义了一些常见的字典操作来遍历这个列表
c = ChainMap(a, b)
# 如果出现重复键，那么第一次出现的映射值会被返回
print(c['x'])  # Outputs 1  (from a)
print(c['y'])  # Outputs 2  (from b)
print(c['z'])  # Outputs 3  (from a)
print(c)
# # Output some common values
print('len(c):', len(c))
print('c.keys():', list(c.keys()))
print('c.values():', list(c.values()))

# # Modify some values
del c['x']
print("a:", a)


# # Example of stacking mappings (like scopes)
values = ChainMap()
values['x'] = 1
# # Add a new mapping
# new_child作用是将一个新的字典加在chainmap头部，返回一个新的chainmap(仍然是引用原来的字典)
values = values.new_child()
values['x'] = 2
# # Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])

# # Discard last mapping
# parents返回一个新的chainMap截取内部list的[1:]
values = values.parents
print(values)
print(values['x'])

# # Discard last mapping
# values = values.parents
# print(values)
# print(values['x'])

# print()
