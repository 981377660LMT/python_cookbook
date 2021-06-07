from enum import Enum


class VIP(Enum):
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
