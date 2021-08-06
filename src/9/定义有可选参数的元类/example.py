# Example of a metaclass that takes optional arguments
# 为了使元类支持这些关键字参数，你必须确保在 __prepare__() , __new__() 和 __init__() 方法中 都使用强制关键字参数。
# __prepare__() 方法在所有类定义开始执行前首先被调用，用来创建类命名空间。 通常来讲，这个方法只是简单的返回一个字典或其他映射对象。
# __new__() 方法被用来实例化最终的类对象。它在类的主体被执行完后开始执行。
#  __init__() 方法最后被调用，用来执行其他的一些初始化工作。


class MyMeta(type):
    # Optional
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        # Custom processing
        return super().__prepare__(name, bases)

    # Required
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        return super().__new__(cls, name, bases, ns)

    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        super().__init__(name, bases, ns)


# Examples
class A(metaclass=MyMeta, debug=True, synchronize=True):
    pass


class B(metaclass=MyMeta):
    pass


class C(metaclass=MyMeta, synchronize=True):
    pass

