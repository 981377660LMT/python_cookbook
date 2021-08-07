# 对于测试很小的代码片段运行性能，使用 timeit 模块会很方便，例如：
from timeit import timeit

# timeit 会执行第一个参数中语句100万次并计算运行时间。
# 第二个参数是运行测试之前配置环境。如果你想改变循环执行次数，
# 可以像下面这样设置 number 参数的值：
print(timeit('math.sqrt(2)', 'import math', number=10000000))
