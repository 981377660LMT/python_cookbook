from collections import defaultdict

# defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要关注添加元素操作了。
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)
a = set([12, 3])
print(a)

# 如果你并不需要这样的特性，你可以在一个普通的字典上使用 setdefault() 方法来代替
d.setdefault(1, []).append(1)
print(d)
