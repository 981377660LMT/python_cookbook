# Example of a generator with extra state that can be
# accessed.   Simply define as a class!

from collections import deque
from io import TextIOWrapper
from os.path import dirname, join

# 将它实现为一个类，然后把生成器函数放到 __iter__() 方法中过去
class linehistory:
    def __init__(self, lines: TextIOWrapper, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open(join(dirname(__file__,), 'somefile.txt')) as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')

