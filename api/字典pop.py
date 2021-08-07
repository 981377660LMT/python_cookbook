dic = {'a': 1, 'b': 2}
print(dic.pop('a'))
print(dic)


fileds = ['a', 'b']
args = [1, 2]
z = zip(fileds, args)
print(list(z))


dic.update(z)
print(dic)