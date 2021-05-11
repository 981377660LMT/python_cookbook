# collections 定义了很多抽象基类，当你想自定义容器类的时候它们会非常有用。
# 比如你想让你的类支持迭代，那就让你的类继承 collections.Iterable 即可
# 不过你需要实现 collections.Iterable 所有的抽象方法，否则会报错:
import collections
import bisect


class A(collections.Iterable):
    pass


class B(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    # 有序添加
    def add(self, item):
        bisect.insort(self._items, item)


class C(collections.Mapping):
    pass


class D(collections.Container):
    pass


# a = A()
b = B()
# c = C()
# d = D()
# 你可以先试着去实例化一个对象，在错误提示中可以找到需要实现哪些方法：
# Can't instantiate abstract class A with abstract methods __iter__
