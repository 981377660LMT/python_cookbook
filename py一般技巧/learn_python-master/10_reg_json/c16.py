import re

s = 'A83C72D1D8E67'

# match从头开始匹配，如果开头没有找到就返回None
# 返回值None
r = re.match('\d', s)
print(r)

# search搜索整个字符串，直到找到第一个才返回
# 返回值<re.Match object; span=(1, 2), match='8'>
r1 = re.search('\d', s)
print(r1)
print(r1.group())
print(r1.span())

r2 = re.findall('\d', s)
print(r2)
