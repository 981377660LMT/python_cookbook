import time


class MyDate:
    """方法一：使用类方法"""

    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


class NewDate(MyDate):
    pass


d = NewDate.today()
# print(d)
#########################################################
class MyAnotherDate:
    """方法二：可以通过 __new__() 方法创建一个未初始化的实例"""

    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = time.localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


d = MyAnotherDate.__new__(MyAnotherDate)
data = {'year': 2021, 'month': 5}
for key, value in data.items():
    setattr(d, key, value)
print(d.year)