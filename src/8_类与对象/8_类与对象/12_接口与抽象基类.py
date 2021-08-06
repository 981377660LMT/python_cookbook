# 定义一个接口或抽象类，并且通过执行类型检查来确保子类实现了某些特定的方法(类实现接口)
#  abc 模块可以很轻松的定义抽象基类
# 抽象基类的一个主要用途是在代码中检查某些类是否为特定类型，实现了特定接口：
# 标准库中有很多用到抽象基类的地方。collections 模块定义了很多跟容器和迭代器(序列、映射、集合等)有关的抽象基类。
# numbers 库定义了跟数字对象(整数、浮点数、有理数等)有关的基类。
# io 库定义了很多跟I/O操作相关的基类。
from abc import ABCMeta, abstractmethod
import collections


# 当作接口使用,不能直接被实例化
class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        raise NotImplementedError()

    @abstractmethod
    def write(self, data):
        raise NotImplementedError()


class MyStream(IStream):
    pass


mystream = MyStream()


# 尽管ABCs可以让我们很方便的做类型检查，但是我们在代码中最好不要过多的使用它。
# 因为Python的本质是一门动态编程语言，
# 其目的就是给你更多灵活性， 强制类型检查或让你代码变得更复杂，这样做无异于舍本求末。