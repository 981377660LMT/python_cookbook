from decimal import Decimal

# 如果你想更加精确(并能容忍一定的性能损耗)，你可以使用 decimal 模块：
print(4.2 + 2.1)
print(Decimal('4.2') + Decimal('2.1'))
