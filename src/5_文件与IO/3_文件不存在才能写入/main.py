# 可以在 open() 函数中使用 x 模式来代替 w 模式的方法来解决这个问题。
# 要注意的是x模式是一个Python3对 open() 函数特有的扩展。 在Python的旧版本或者是Python实现的底层C函数库中都是没有这个模式的
try:
    with open('somefile', 'xt') as f:
        f.write('Hello\n')
except FileExistsError:
    print('已存在文件')

