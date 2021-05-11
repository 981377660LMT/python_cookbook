from collections import deque
import os
# 在队列两端插入或删除元素时间复杂度都是 O(1) ，
# 区别于列表，在列表的开头插入或删除元素的时间复杂度为 O(N) 。


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'somefile.txt')) as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
