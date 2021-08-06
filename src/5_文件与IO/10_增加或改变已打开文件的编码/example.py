# Example of adding a text encoding to existing file-like object

import urllib.request
import io
import sys

# 如果你想给一个以二进制模式打开的文件添加Unicode编码/解码方式， 可以使用 io.TextIOWrapper() 对象包装它
# u = urllib.request.urlopen('http://www.python.org')
# f = io.TextIOWrapper(u, encoding='utf-8')
# text = f.read()

# print(text)

########
with open('test.py', 'r') as f:
    print(f)
    print(f.buffer)
    print(f.buffer.raw)
# <_io.TextIOWrapper name='test.py' mode='r' encoding='cp936'>
# <_io.BufferedReader name='test.py'>
# <_io.FileIO name='test.py' mode='rb' closefd=True>

# io.TextIOWrapper 是一个编码和解码Unicode的文本处理层，
# io.BufferedWriter 是一个处理二进制数据的带缓冲的I/O层
# io.FileIO 是一个表示操作系统底层文件描述符的原始文件
# 增加或改变文本编码会涉及增加或改变最上面的 io.TextIOWrapper 层。
# I/O系统以层级结构的形式构建而成。
# 文本文件是通过在一个拥有缓冲的二进制模式文件上增加一个Unicode编码/解码层来创建
