# deque是双向列队
from collections import deque
a = deque([1, 2, 3, 4], maxlen=4)
print(a)
# deque([1, 2, 3, 4], maxlen=4)
a.append(5)
print(a)
deque([2, 3, 4, 5], maxlen=4)
