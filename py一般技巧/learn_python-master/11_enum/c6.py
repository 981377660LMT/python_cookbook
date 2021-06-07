from enum import Enum
from enum import IntEnum, unique


# 枚举的值只能是int，且必须唯一
@unique
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


# 23种设计模式 单例模式
