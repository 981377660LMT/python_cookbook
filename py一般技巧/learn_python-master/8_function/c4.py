a = 1
b = 2
c = 3

a, b, c = 1, 2, 3

d = 1, 2, 3
print(type(d))

a, b, c = d
print(a, b, c)

# 下面这种写法是错误的
# a, b = (1, 2, 3)

a = 1
b = 1
c = 1
a, b, c = 1, 1, 1
a = b = c = 1
