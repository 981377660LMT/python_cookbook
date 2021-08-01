# example.py
#
# Examples of simple regular expression substitution
# 搜索:findAll
import re

# (b) Replacement function
from calendar import month_abbr
from typing import Match

# Some sample text
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

# 如果你想使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象
# 在定义正则式的时候，通常会利用括号去捕获分组
# 核心步骤就是先使用 re.compile() 编译正则表达式字符串， 然后使用 match() , findall() 或者 finditer() 等方法。
# r字符串将不去解析反斜杠
datepat = re.compile(r'(\d+)/(\d+)/(\d+)', flags=re.IGNORECASE)

print(datepat.findall(text))
#################################################
# 替换:sub/replace
# (a) Simple substitution
print(datepat.sub(r'\3-\1-\2', text))

# 一个替换回调函数的参数是一个 match 对象
def change_date(m: Match):
    # m.group()是整个字符串
    print('here', m.group())
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


print(datepat.sub(change_date, text))
