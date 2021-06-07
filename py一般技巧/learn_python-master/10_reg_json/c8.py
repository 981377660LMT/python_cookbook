# 数量词
import re
a = 'python 1111java678php'

# 匹配3次：[a-z]{3}
# 匹配3-6次：[a-z]{3,6}

# 贪婪 与 非贪婪

# 默认是贪婪
r = re.findall('[a-z]{3,6}', a)
print(r)

# 范围后面加个?是非贪婪
r = re.findall('[a-z]{3,6}?', a)
print(r)

# * 匹配0次或者无限多次
a = 'pytho0python1pythonn2'
r = re.findall('python*', a)
print(r)

# + 匹配1次或者无限多次
r = re.findall('python+', a)
print(r)

# ? 匹配0次或者1次
r = re.findall('python?', a)
print(r)
