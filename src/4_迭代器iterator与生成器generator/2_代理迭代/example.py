# example.py
#
# Example of depth-first search using a generator

# 迭代node


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    # __iter__() 方法只是简单的将迭代请求传递给内部的 _children 属性
    # iter(s) 只是简单的通过调用 s.__iter__() 方法来返回对应的迭代器对象，
    # 就跟 len(s) 会调用 s.__len__() 原理是一样的
    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        # yield self出去 in self会调用 self的__iter__
        yield self
        for c in self:
            # yield from iterable 同JS 的yield*
            # The yield* expression is used to delegate to another generator(iterable) or iterable object.
            yield from c.depth_first()


# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
    # Outputs: Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)
