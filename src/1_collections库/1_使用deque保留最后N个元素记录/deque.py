# deque是双向列队
from collections import deque
from typing import Iterable

a = deque([1, 2, 3, 4], maxlen=4)
print(a)
# deque([1, 2, 3, 4], maxlen=4)
a.append(5)
print(list(a), isinstance(a, Iterable))
deque([2, 3, 4, 5], maxlen=4)
