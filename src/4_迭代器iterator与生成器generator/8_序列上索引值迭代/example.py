# Example of iterating over lines of a file with an extra lineno attribute
from os.path import dirname, join

# 你想在迭代一个序列的同时跟踪正在被处理的元素索引。
# 这种情况在你遍历文件时想在错误消息中使用行号定位时候非常有用

def parse_data(filename):
    with open(filename, 'rt') as f:
        # 按传统行号输出(指定行号从1开始)
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))


parse_data(join(dirname(__file__), 'sample.dat'))
