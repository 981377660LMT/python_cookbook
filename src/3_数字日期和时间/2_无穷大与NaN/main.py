import math

# Python并没有特殊的语法来表示这些特殊的浮点值，但是可以使用 float() 来创建它们
# 想了解更多这些特殊浮点值的信息，可以参考IEEE 754规范
print(float('inf'))
print(float('-inf'))
c = float('nan')

print(math.isnan(c))

# 无穷大数在执行数学计算的时候会传播,但是有些操作时未定义的并会返回一个NaN结果
# NaN值会在所有操作中传播，而不会产生异常
# NaN值的一个特别的地方时它们之间的比较操作总是返回False
