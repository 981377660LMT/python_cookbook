from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


class VIP1(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


print(VIP.YELLOW)
print(VIP.YELLOW.value)
print(VIP.YELLOW.name)
print(type(VIP.YELLOW))
print(type(VIP.YELLOW.value))
print(type(VIP.YELLOW.name))

print(VIP['GREEN'])

# 枚举类型、枚举的名字、枚举的值

for v in VIP:
    print(v)


result = VIP.GREEN == VIP.BLACK
print(result)
print(VIP.GREEN == VIP.GREEN)
# print(VIP.GREEN > VIP.GREEN)
print(VIP.GREEN is VIP.GREEN)
print(VIP.GREEN == VIP1.GREEN)


class VIP2(Enum):
    YELLOW = 1
    GREEN = 1       # GREEN是YELLOW的别名
    BLACK = 3
    RED = 4


print('VIP2.GREEN =', VIP2.GREEN)

for v in VIP2:
    print(v)

for v in VIP.__members__.items():
    print(v)

# 如何将数字转化为枚举类型
a = 1
print(VIP(a))
