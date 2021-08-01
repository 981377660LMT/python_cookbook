# 一个函数中需要有一个 yield 语句即可将其转换为一个生成器
#  跟普通函数不同的是，生成器只能用于迭代操作。

# 一个生成器函数主要特征是它只会回应在迭代中使用到的 next 操作
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)
