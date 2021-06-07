list_x = [1, 0, 1, 0, 0, 1]
# filter第一个参数必须返回True或False
r = filter(lambda x: True if x == 1 else False, list_x)
# r = filter(lambda x: x, list_x)
print(list(r))

list_u = ['a', 'B', 'c', 'F', 'e']
r = filter(lambda x: True if 'a' <= x <= 'z' else False, list_u)
print(list(r))
