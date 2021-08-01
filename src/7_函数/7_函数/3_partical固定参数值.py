# artial() 可以更加直观的表达你的意图(给某些参数预先赋值)。
import math
from functools import partial


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


points = [(1, 2), (3, 4), (2, 3), (1, 1)]
# 到(2,2)的距离进行排序

# 相当于points.sort(key=lambda point: distance(point, (2, 2)))
points.sort(key=partial(distance, (2, 2)))

print(points)
