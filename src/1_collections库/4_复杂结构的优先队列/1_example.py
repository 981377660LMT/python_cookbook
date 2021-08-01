# example.py
#
# Example of a priority queue

import heapq


class PriorityQueue:
    """
    队列由 (priority, index, item) 形式组成
    priority 增加 "-" 号是因为 heappush 默认是最小堆
    index 是为了当两个对象的优先级一致时，按照插入顺序排列
    """

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # python排序元组、列表时
        # 当一个对象的所有元素都是可比较的时，
        # 默认情况下是根据队列中的对象的第一个元素进行排序，
        # 越小的优先级越高，排在越前面。
        # _index的作用是当第一个元素相同时，依次比较后续的元素的大小(即插入顺序)来进行排序。
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # 返回弹出的-priority, self._index, item)元组中最后一项Item
        return heapq.heappop(self._queue)[-1]


# Example use
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
# 可知(-5,1,Item(bar))是最小堆堆顶元素
# heappop() 函数总是返回”最小的”的元素
print("Should be bar:", q.pop())
print(q.__dict__)
print("Should be spam:", q.pop())
print("Should be foo:", q.pop())
print("Should be grok:", q.pop())

# 如果你想在多个线程中使用同一个队列，那么你需要增加适当的锁和信号量机制。
# 使用queue的PQ
