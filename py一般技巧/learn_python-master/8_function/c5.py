# 参数
# 1. 必须参数
# 2. 关键字参数
# 3. 默认参数
# 4. 可变参数


def add(x, y):
    # 形式参数，形参
    result = x + y
    return result


# 关键字参数增加可读性
c = add(y=3, x=2)
