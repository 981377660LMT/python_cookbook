import re

a = 'C|C++|Java|C#|Python|Javascript'


# print(a.index('Python') > -1)
# print('Python' in a)

r = re.findall('PHP', a)
print(r)
# 规则
if len(r) > 0:
    print('字符串中包含PHP')
else:
    print('No')
