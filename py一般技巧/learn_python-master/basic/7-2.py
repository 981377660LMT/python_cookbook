# 主要是用来遍历/循环，序列或者集合、字典
a = [['apple', 'orange', 'banana', 'grape'],
     (1, 2, 3)]
for x in a:
    if 'banana' in x:
        break
    for y in x:
        if y == 'orange':
            break
        print(y, end='\n')
else:
    print('fruit is gone')

a = [1, 2, 3]
for x in a:
    if x == 2:
        break
    print(x)
else:
    # 如果不是正常结束，就不会打印，break就是非正常退出
    print('EOF')

for x in range(10, 0, -2):
    print(x, end=' | ')
else:
    print('')

a = [1, 2, 3, 4, 5, 6, 7, 8]
for x in range(0, len(a), 2):
    print(a[x], end=' | ')
else:
    print('')


b = a[0:len(a):2]
print(b)
