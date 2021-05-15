# Class just to illustrate when deletion occurs
class Data:
    def __del__(self):
        print('Data.__del__')


# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    # 父节点和孩子节点互相拥有对方的引用，导致每个对象的引用计数都不可能变成0。
    def add_child(self, child):
        self.children.append(child)
        child.parent = self


a = Node()

a.add_child(Node())
print(1)
del a
print(2)