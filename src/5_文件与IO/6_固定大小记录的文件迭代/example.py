# Example of iterating of fixed-size records
#
# The file 'data.bin' contains 32-byte fixed size records
# that consist of a 4-digit number followed by a 28-byte string.
# 你想在一个固定长度记录或者数据块的集合上迭代，而不是在一个文件中一行一行的迭代。

from functools import partial

RECORD_SIZE = 32

with open('data.bin', 'rb') as f:
    # iter() 函数有一个鲜为人知的特性就是，如果你给它传递一个可调用对象和一个标记值，它会创建一个迭代器。 这个迭代器会一直调用传入的可调用对象直到它返回标记值为止，这时候迭代终止。
    # functools.partial 用来创建一个每次被调用时从文件中读取固定数目字节的可调用对象
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r, end='okokoko')

# 二进制模式打开,读取固定大小的记录常见
# 而对于文本文件，一行一行的读取(默认的迭代行为)更普遍点。