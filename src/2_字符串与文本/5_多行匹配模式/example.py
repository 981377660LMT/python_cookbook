# example.py
#
# Regular expression that matches multiline patterns

import re

text = '''/* this is a
              multiline comment */
'''

# ?:非捕获分组
# .|\n表示任意字符(除开换行)与换行
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text))
