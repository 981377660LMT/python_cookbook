import sys


def get_cur_info():
    # 当前文件名，可以通过__file__获得
    print(sys._getframe().f_code.co_filename)
    # 当前函数名
    print(sys._getframe(0).f_code.co_name)
    # 调用该函数的函数的名字
    print(sys._getframe(1).f_code.co_name)
    print(sys._getframe(1).f_locals)


get_cur_info()
# print sys._getframe().f_locals，这个等价于
# print locals()，不同的在于_getframe()是返回堆栈上的数据，参数表示栈的深度，默认参数是0，表示返回最顶层的堆栈，当然你可以指定堆栈的深度，比如你可以指定深度为1，在这个例子里面
# print sys._getframe(0).f_locals 等价于 print locals()
# print sys._getframe(1).f_locals 等价于 print globals()
# 当一行代码要使用变量 x 的值时，Python 会到所有可用的名字空间去查找变量，查找的顺序为：
# ● locals    局部名字空间
# ● module globals    全局名字空间 - 特指当前的模块
# ● built-ins    内置名字空间
