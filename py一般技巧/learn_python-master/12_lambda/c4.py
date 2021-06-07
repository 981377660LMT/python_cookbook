from functools import reduce

# 连续计算，连续调用lambda
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
# ((1+2)+3)+4……
# reduce第三个参数是初始值
r = reduce(lambda x, y: x + y, list_x, 10)
print(r)


list = [(1,3),(2,-2),(-2,3)]
r = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), list)
print(r)


# map/reduce 编程模型，映射，规约，并行计算
