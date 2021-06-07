# def gen_func():
#     yield 1
#     name = "bobby"
#     yield 2
#     age = 30
#     return "imooc"


# g = gen_func()

# print(g.__next__(), g.gi_frame.f_lasti, g.gi_frame.f_locals)
# print(g.__next__(), g.gi_frame.f_lasti, g.gi_frame.f_locals)
# print(g.__next__(), g.gi_frame.f_lasti, g.gi_frame.f_locals)

# JS里
# return为迭代器的最后一次迭代（当done等于时true）提供返回值。
# 如果使用for ... of循环或类似方法通过迭代器进行迭代Array.from，则该return值将被忽略
from collections import UserList
