# example.py
#
# Examples of reformatting text to different column widths

# A long string
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap
import os

print(textwrap.fill(s, 70))
print()

print(textwrap.fill(s, 40))
print()

print(textwrap.fill(s, 40, initial_indent='    '))
print()

print(textwrap.fill(s, 40, subsequent_indent='    '))
print()

# 当你希望输出自动匹配终端大小的时候。 你可以使用 os.get_terminal_size() 方法来获取终端的大小尺寸
print(os.get_terminal_size())