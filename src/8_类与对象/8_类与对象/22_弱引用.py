import weakref

# Node class involving a cycle
class Node:
    def __init__(self):
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


a = Node()
a_ref = weakref.ref(a)
print(a_ref())
# 弱引用就是一个对象指针，它不会增加它的引用计数
# 为了访问弱引用所引用的对象，你可以像函数一样去调用它即可。如果那个对象还存在就会返回它，否则就返回一个None。 由于原始对象的引用计数没有增加，那么就可以去删除它了。