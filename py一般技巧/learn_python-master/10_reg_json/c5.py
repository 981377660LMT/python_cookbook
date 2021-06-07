# 概括字符集

# \d 数字
# \D 非数字
# \w 单词字符
# \W 非单词字符
# \s 空白字符
# \S 非空白字符
# . 匹配除换行符\n之外其他所有字符
import re
a = 'python 1111\njava&_678php'

# \d等价于[0-9]
# \D等价于[^0-9]
# \w等价于[A-Za-z0-9_]
# \W等价于[^A-Za-z0-9_]
# \s等价于[ \n\r\t]
# \S等价于[^ \n\r\t]
r = re.findall('\s', a)
print(r)
