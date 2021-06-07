import sys
# 设置递归的最大层数
# sys.setrecursionlimit(10000000)


def funcname(parameter_list):
    pass


# 1. 参数列表可以没有
# 2. return value   None


# 1. 实现两个数字的相加
# 2. 打印输入的参数
def add(x, y):
    # 形式参数，形参
    result = x + y
    return result


def print_code(code):
    print(code)


a = add(1, 2)   # 实际参数，实参
b = print_code('Python')

print(a, b)
