# redis缓存策略之一LRU
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity) -> None:
        self.od = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.od:
            val = self.od[key]
            # 移到右边
            self.od.move_to_end(key)
            return val
        else:
            return -1

    def put(self, key, value):
        if key in self.od:
            del self.od[key]
            self.od[key] = value
        else:
            if len(self.od) >= self.capacity:
                # 删除最左边的
                self.od.popitem(last=False)
                self.od[key] = value
