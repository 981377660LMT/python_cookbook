import re

s = 'life is short, i use python, i love python'
# None
r = re.search('life(.*)python(.*)python', s)
print(r.group())
print(r.group(0))
print(r.group(1))
print(r.group(2))
# 返回('life is short, i use python, i love python', ' is short, i use ', ', i love ')
print(r.group(0, 1, 2))
# 返回(' is short, i use ', ', i love ')
print(r.groups())

# 这个会返回[' is short, i use ']
r = re.findall('life(.*)python', s)
print(r)
