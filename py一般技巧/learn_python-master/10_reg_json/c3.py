import re

a = 'C0C++7Java8C#9Python6Javascript'

# Python    普通字符
# \d        元字符

r = re.findall('\D', a)
print(r)
