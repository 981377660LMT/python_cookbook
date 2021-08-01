record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)
# 代码中如果出现大量的硬编码下标会使得代码的可读性和可维护性大大降低
print(SHARES.indices(2))

# 通过调用切片的 indices(size) 方法将它映射到一个已知大小的序列上。
# 这个方法返回一个三元组 (start, stop, step) ，
# 所有的值都会被缩小，直到适合这个已知序列的边界为止。
s = "NoIndexError"
foo = slice(5, 19, 2)
print(foo.indices(len(s)))
for i in range(*foo.indices(len(s))):
    print(i)

