# example.py
#
# Example of a tokenizer

# 你有一个字符串，想从左至右将其解析为一个令牌流。
# text = 'foo = 23 + 42 * 10'
# tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
#           ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

import re
from collections import namedtuple
from typing import Pattern

# 第一步就是像下面这样利用命名捕获组的正则表达式来定义所有可能的令牌，包括空格
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

Token = namedtuple('Token', ['type', 'value'])


# 从pattern构建扫描器
def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

# 令牌化是很多高级文本解析与处理的第一步
