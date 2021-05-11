# 迭代器，生成器，文件都可以解构
from collections import Iterable
print(isinstance('abcde', Iterable))
a,  *_,  e = 'abcde'
print(e)


# ###############################################
# # 关于迭代器和生成器
# # 生成器generator
# # 只要把一个列表生成式的[]中括号改为（）小括号，就创建一个generator
# generator_test = (i for i in range(3))
# # 如果要一个个打印出来，可以通过next（）函数获得generator的下一个返回值
# for i in generator_test:
#     print(i)


# # 函数用生成器实现
# # 到yield处函数停止，再调用程序从yield处继续向下执行
# # 生成器属于迭代器，迭代器都有一个__next__()__成员方法，这个方法要么返回迭代的下一项，要买引起异常结束迭代。
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a+b
#         n = n+1
#     return 'done'


# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('generator: ', x)
#     except StopIteration as e:
#         print("生成器返回值：", e.value)
#         break

# #########################################
# #  map 返回是迭代器
# # info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # a = map(lambda x: x+1, info)
# # print(list(a))
