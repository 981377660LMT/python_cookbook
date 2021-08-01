# example.py
#
# Find out what two dictionaries have in common

a = {'x': 1, 'y': 2, 'z': 3}

b = {'w': 10, 'x': 11, 'y': 2}
print(list(a.items()))
print('Common keys:', a.keys() & b.keys())
print('Keys in a not in b:', a.keys() - b.keys())
print('(key,value) pairs in common:', a.items() & b.items())
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
#  字典的 keys() 方法返回一个展现键集合的键视图KeysView对象 它们也支持集合操作
# items() 方法返回一个包含 (键，值) 对的元素视图对象ItemsView。 这个对象同样也支持集合操作

# 字典的 values() 方法并不支持这里介绍的集合操作
