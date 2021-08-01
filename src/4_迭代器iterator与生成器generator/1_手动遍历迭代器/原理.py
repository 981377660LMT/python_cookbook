class Foo:
    def __iter__(self):
        print('symbol.iterator')
        yield 1
        # return iter([1, 2, 3])


f = Foo()
for i in f:
    print(i)

