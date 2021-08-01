from itertools import islice


def count(n):
    while True:
        yield n
        n += 1


c = count(0)

# 生成指定元素的迭代器，它通过遍历并丢弃直到切片开始索引位置的所有元素。
# 然后才开始一个个的返回元素，并直到切片结束索引位置。
for i in islice(c, 10, 20, 2):
    print(i)

# 这里要着重强调的一点是 islice() 会消耗掉传入的迭代器中的数据。
# 必须考虑到迭代器是不可逆的这个事实。
# 所以如果你需要之后再次访问这个迭代器的话，
# 那你就得先将它里面的数据放入一个列表中。
