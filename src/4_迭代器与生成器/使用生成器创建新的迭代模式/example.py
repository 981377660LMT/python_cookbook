# 一个函数中需要有一个 yield 语句即可将其转换为一个生成器
#  跟普通函数不同的是，生成器只能用于迭代操作。

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)
