# 一个描述器就是一个实现了三个核心的属性访问操作(get, set, delete)的类， 分别为 __get__() 、__set__() 和 __delete__() 这三个特殊的方法。
# 这些方法接受一个实例作为输入，之后相应的操作实例底层的字典。
# 描述器只能在类级别被定义，而不能为每个实例单独定义。

# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls

    return decorate


# Example use
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


#########################################
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print(instance, cls)
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


# __get__() 如果一个描述器被当做一个类变量来访问，那么 instance 参数被设置成 None，cls是类
# __get__() 如果一个描述器被当做一个实例变量来访问，那么 instance 参数是实例对象，cls是instance的类
p = Point(2, 3)
print(p.x)
print(Point.x

# 如果一个对象同时定义了 __get__() 和 __set__(),它叫做资料描述器(data descriptor)。
# 仅定义了 __get__() 的描述器叫非资料描述器(常用于方法，当然其他用途也是可以的)

a = {}
print('a' not in a)
