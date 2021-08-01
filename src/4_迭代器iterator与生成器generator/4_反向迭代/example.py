# Example of an object implementing both forward and reversed iterators
# 要注意的是如果可迭代对象元素很多的话，将其预先转换为一个列表要消耗大量的内存

# 可以通过在自定义类上实现 __reversed__() 方法来实现反向迭代
class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


c = Countdown(5)
print("Forward:")
for x in c:
    print(x)

print("Reverse:")
for x in reversed(c):
    print(x)
