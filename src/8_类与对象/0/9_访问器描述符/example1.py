# Descriptor attribute for an integer type-checked attribute
# 是它只能在类级别被定义，而不能为每个实例单独定义
# 如果一个描述器被当做一个类变量来访问，那么 instance 参数被设置成 None 。
class Integer:
    def __init__(self, name):
        self.name = name

    # __get__() 看上去有点复杂的原因归结于实例变量和类变量的不同
    def __get__(self, instance, cls):
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


if __name__ == '__main__':
    p = Point(2, 3)
    print(p.x)
    p.y = 5
    try:
        p.x = 2.3
    except TypeError as e:
        print(e)
