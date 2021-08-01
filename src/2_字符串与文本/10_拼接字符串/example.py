# example.py
#
# Example of combining text via generators
# 字符串是在一个序列或者 iterable 中，那么最快的方式就是使用 join() 方法
# 这种语法看上去会比较怪，但是 join() 被指定为字符串的一个方法
# 但是列表，元组，字典，文件，集合或生成器等如果在所有这些对象上都定义一个 join() 方法明显是冗余的
# 使用加号(+)操作符去连接大量的字符串的时候是非常低效率的， 因为加号连接会引起内存复制以及垃圾回收操作
# 每一次执行+=操作的时候会创建一个新的字符串对象。 你最好是先收集所有的字符串片段然后再将它们连接起来。


def sample():
    yield "Is"
    yield "Chicago"
    yield "Not"
    yield "Chicago?"


# (a) Simple join operator
text = ' '.join(sample())
print(text)

# (b) Redirection of parts to I/O
# 字符串片段重定向到I/O
import sys
from typing import Generator

for part in sample():
    sys.stdout.write(part)
sys.stdout.write('\n')


# (c) Combination of parts into buffers and larger I/O operations
def combine(source: Generator, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    # 最后读完文件将剩余的yielf
    yield ''.join(parts)


for part in combine(sample(), 32768):
    sys.stdout.write(part)
sys.stdout.write('\n')

