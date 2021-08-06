from functools import wraps
from queue import Queue


def apply_async(func, *args, callback):
    result = func(*args)

    callback(result)


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        # f是生成器
        f = func(*args)
        result_queue = Queue()
        # 激活
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a: Async = f.send(result)
                # 将生成器的yield放入result_queue
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break

    return wrapper


@inlined_async
def test():
    r = yield Async(sum, (2, 3))
    print(r)
    r = yield Async(sum, (1, 2))
    print(r)
    for n in range(10):
        r = yield Async(sum, (n, n))
        print(r)
    print('Goodbye')


# Run the test function
test()

# 根据这个思路，这一小节的核心就在 inline_async() 装饰器函数中了。
#  关键点就是，装饰器会逐步遍历生成器函数的所有 yield 语句，每一次一个。
# 为了这样做，刚开始的时候创建了一个 result 队列并向里面放入一个 None 值。
# 然后开始一个循环操作，从队列中取出结果值并发送给生成器，它会持续到下一个 yield 语句，
# 在这里一个 Async 的实例被接受到。然后循环开始检查函数和参数，并开始进行异步计算 apply_async() 。
# 然而，这个计算有个最诡异部分是它并没有使用一个普通的回调函数，而是用队列的 put() 方法来回调。
