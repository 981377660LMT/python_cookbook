# TODO

# 如果一个描述仅仅是从底层实例字典中获取某个属性值的话，那么没必要去定义 __get__() 方法。
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int


class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance, value)


# 所有描述器类都是基于混入类来实现的。
# 混入类的一个比较难理解的地方是，调用 super() 函数时，你并不知道究竟要调用哪个具体类。 你需要跟其他类结合后才能正确的使用，也就是必须合作才能产生效果。
class UnsignedInteger(Integer, Unsigned):
    pass


# 装饰器还能作为混入类的替代技术来实现同样的效果;
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p13_implementing_data_model_or_type_system.html