class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B2:
    """使用__getattr__的代理，代理方法比较多时候"""

    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    # Expose all of the methods defined on class A
    def __getattr__(self, name):
        """这个方法在访问的attribute不存在的时候被调用
        the __getattr__() method is actually a fallback method
        that only gets called when an attribute is not found"""
        return getattr(self._a, name)


b = B2()
b.bar()
b.spam(42)

###########################################
# A proxy class that wraps around another object, but
# exposes its public attributes

# getattr, setattr, delattr类比js里Reflect上的几个方法


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)

    # Delegate attribute assignment
    # 代理类只暴露被代理类的公共属性
    def __setattr__(self, name, value):
        if name.startswith('_'):
            # 这里的super即为Proxy类实例
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    # Delegate attribute deletion
    # 代理类只暴露被代理类的公共属性
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)


s = Spam(2)
p = Proxy(s)
p._x = 37
# 当实现代理模式时，还有些细节需要注意。
# 首先，__getattr__() 实际是一个后备方法，只有在属性不存在时才会调用。
# 因此，如果代理类实例本身有这个属性的话，那么不会触发这个方法的。
# 另外，__setattr__() 和 __delattr__() 需要额外的魔法来区分代理实例和被代理实例 _obj 的属性。
# 一个通常的约定是只代理那些不以下划线 _ 开头的属性(代理类只暴露被代理类的公共属性)。

# 还有一点需要注意的是，__getattr__() 对于大部分以双下划线(__)开始和结尾的属性并不适用。
# 例如__len__
class ListLike:
    """__getattr__对于双下划线开始和结尾的方法是不能用的，需要一个个去重定义"""

    def __init__(self):
        self._items = []

    def __getattr__(self, name):
        return getattr(self._items, name)

    # Added special methods to support certain list operations
    def __len__(self):
        return len(self._items)


a = ListLike()
a.append(1)
print(len(a))