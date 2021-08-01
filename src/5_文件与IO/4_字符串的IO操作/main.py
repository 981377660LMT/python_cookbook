# 使用 io.StringIO() 和 io.BytesIO() 类来创建类文件对象操作字符串数据
from io import StringIO, BytesIO

# 在单元测试中，你可以使用 StringIO 来创建一个包含测试数据的类文件对象
# 这个对象可以被传给某个参数为普通文件对象的函数。
# StringIO 和 BytesIO 实例并没有正确的整数类型的文件描述符
# 因此，它们不能在那些需要使用真实的系统级文件如文件，管道或者是套接字的程序中使用
s = StringIO()
s.write('Hello World\n')
print('Test', file=s)
print(s.getvalue())

b = BytesIO()
b.write(b'asas')
print(b.getbuffer(), b.getvalue())

