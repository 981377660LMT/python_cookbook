# 将一个只读属性定义成一个property，并且只在访问的时候才会计算结果。
#  但是一旦被访问后，你希望结果值被缓存起来，不用每次都去计算。

# 一个延迟属性的一种高效方法是通过使用一个描述器类
# 1.如何lazy:get时才赋值
# 2.如何缓存：装饰器，把函数缓存在LazyProperty里；get时计算值，把值附加在实例上。
import math

# 描述器
# 当一个描述器被放入一个类的定义时， 每次访问属性时它的 __get__() 、__set__() 和 __delete__() 方法就会被触发。
# 特别地，只有当被访问属性不在实例底层的字典中时 __get__() 方法才会被触发。
class LazyProperty:
    def __init__(self, func) -> None:
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            # 相当于func.apply(this)
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    @LazyProperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @LazyProperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


c = Circle(4.0)

print(Circle.area)
# <__main__.LazyProperty object at 0x000001D0AEDA8910>

# 实例上没有area，在类上找
print(c.area)
# Computing area
# 50.26548245743669

# 实例上有area
print(c.area)
# 50.26548245743669


# 如果你担心计算出的值被创建后是可以被修改，那么可以使用一种稍微没那么高效的实现
# 有一个缺点就是所有get操作都必须被定向到属性的 getter 函数上去。
def lazyproperty(func):
    name = '_lazy_' + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value

    return lazy
