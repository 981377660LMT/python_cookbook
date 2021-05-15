# 装饰器 functools.total_ordering 就是用来简化这个处理的。
# 使用它来装饰一个类，你只需定义一个 __eq__() 方法，
# 外加其他方法(__lt__, __le__, __gt__, or __ge__)中的一个即可。
#  然后装饰器会自动为你填充其它比较方法。
from functools import total_ordering


class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width


@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return '{}: {} square foot {}'.format(self.name, self.living_space_footage, self.style)

    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage


# 这里我们只是给House类定义了两个方法：__eq__() 和 __lt__() ，它就能支持所有的比较操作：
# Build a few houses, and add rooms to them
h1 = House('h1', 'Cape')
h1.add_room(Room('Master Bedroom', 14, 21))
h1.add_room(Room('Living Room', 18, 20))
h1.add_room(Room('Kitchen', 12, 16))
h1.add_room(Room('Office', 12, 12))
h2 = House('h2', 'Ranch')
h2.add_room(Room('Master Bedroom', 14, 21))
h2.add_room(Room('Living Room', 18, 20))
h2.add_room(Room('Kitchen', 12, 16))
h3 = House('h3', 'Split')
h3.add_room(Room('Master Bedroom', 14, 21))
h3.add_room(Room('Living Room', 18, 20))
h3.add_room(Room('Office', 12, 16))
h3.add_room(Room('Kitchen', 15, 17))
houses = [h1, h2, h3]
print('Is h1 bigger than h2?', h1 > h2)  # prints True


# # 怎么做到的?
# 等于不等于 大于不大于 小于不小于
# class House:
#     def __eq__(self, other):
#         pass

#     def __lt__(self, other):
#         pass

#     # Methods created by @total_ordering
#     __le__ = lambda self, other: self < other or self == other
#     __gt__ = lambda self, other: not (self < other or self == other)
#     __ge__ = lambda self, other: not (self < other)
#     __ne__ = lambda self, other: not self == other
