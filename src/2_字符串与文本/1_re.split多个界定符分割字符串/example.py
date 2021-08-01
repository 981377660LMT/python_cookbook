# example.py
#
# Example of splitting a string on multiple delimiters using a regex

import re

line = 'asdf fjdk; afed, fjek,asdf,      foo'

# (a) Splitting on space, comma, and semicolon
parts = re.split(r'\s*[;,\s]\s*', line)
print(parts)

# # (b) Splitting with a capture group
# 当你使用 re.split() 函数时候，需要特别注意的是正则表达式中是否包含一个括号捕获分组
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

# # (c) Rebuilding a string using fields above
values = fields[::2]
delimiters = fields[1::2]
delimiters.append('')
print('value =', values)
print('delimiters =', delimiters)
newline = ''.join(v + d for v, d in zip(values, delimiters))
print('newline =', newline)

# # (d) Splitting using a non-capture group
# 不想保留分割字符串到结果列表中去但仍然需要使用到括号来分组正则表达式的话 使用非捕获分组(?)
parts = re.split(r'(?:,|;|\s)\s*', line)
print(parts)
