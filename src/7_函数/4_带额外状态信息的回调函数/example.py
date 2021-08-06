# This example is about the problem of carrying extra state around
# through callback functions.   To test the examples, this very
# simple code emulates the typical control of a callback.

# 如果你想让回调函数连续执行多步操作， 那你就必须去解决如何保存和恢复相关的状态信息了。

# 实际上，这段代码可以做任何更高级的处理，包括线程、进程和定时器
def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


# A simple function for testing
def add(x, y):
    return x + y


# (a) A simple callback example

print('# --- Simple Example')


def print_result(result):
    print("Got:", result)


apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('hello', 'world'), callback=print_result)
######################################################################
# (b) Using a bound method
# 使用一个绑定方法来代替一个简单函数
print('# --- Using a bound-method')


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ('hello', 'world'), callback=r.handler)
######################################################################
# (c) Using a closure
# 作为类的替代，可以使用一个闭包捕获状态值
# 闭包或许是更加轻量级和自然一点，因为它们可以很简单的通过函数来构造。 它们还能自动捕获所有被使用到的变量

print('# --- Using a closure')


def make_handler():
    sequence = 0

    def handler(result):
        # nonlocal 声明语句用来指示接下来的变量会在回调函数中被修改
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler


clo_handler = make_handler()
apply_async(add, (2, 3), callback=clo_handler)
apply_async(add, ('hello', 'world'), callback=clo_handler)

######################################################################
# (d) Using a coroutine
# 另外一个更高级的方法，可以使用协程来完成同样的事情
# 而使用一个协程来作为一个回调函数就更有趣了，它跟闭包方法密切相关。 某种意义上来讲，它显得更加简洁，因为总共就一个函数而已
# 对于协程，你需要使用它的 send() 方法作为回调函数
print('# --- Using a coroutine')


def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


co_handler = make_handler()
next(co_handler)  # Advance to the yield 预激协程

apply_async(add, (2, 3), callback=co_handler.send)
apply_async(add, ('hello', 'world'), callback=co_handler.send)
######################################################################

# (e) Partial function application
# 如果你仅仅只需要给回调函数传递额外的值的话，还有一种使用 partial() 的方式也很有用
print('# --- Using partial')


class SequenceNo:
    def __init__(self):
        self.sequence = 0


def handler(result, seq):
    seq.sequence += 1
    print('[{}] Got: {}'.format(seq.sequence, result))


seq = SequenceNo()
from functools import partial

apply_async(add, (2, 3), callback=partial(handler, seq=seq))
apply_async(add, ('hello', 'world'), callback=partial(handler, seq=seq))

