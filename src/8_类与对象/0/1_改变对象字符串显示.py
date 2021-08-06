class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x}, {0.y})'.format(self)

    # !r 格式化代码指明输出使用 __repr__() 来代替默认的 __str__()


# 如果 __str__() 没有被定义，那么就会使用 __repr__() 来代替输出

p = Pair(3, 4)
print('p is {0!r} '.format(p))
print('p is {0} '.format(p))
