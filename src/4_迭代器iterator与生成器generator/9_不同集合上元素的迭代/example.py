# Example of iterating over two sequences as one
# a + b 操作会创建一个全新的序列并要求a和b的类型一致。
#  chian() 不会有这一步，所以如果输入序列非常大的时候会很省内存
#  并且当可迭代对象类型不一样的时候 chain() 同样可以很好的工作。


from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)
