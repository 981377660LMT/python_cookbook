# ref=object()

# def bar(a,b=ref):
#   if b is ref:
#     print('b没传')

# print(id(object()),id(object()))
# print(object() is object())

# bar(1)
# #######################################
# lambda 函数绑定变量的值
# x = 10
# a = lambda y: x + y
# b = lambda y, x=x: x + y
# x = 20


# print(a(10), b(10))
# n=n绑定变量,lambda定义时就能绑定到值


# funclist = [lambda x, n=n: x + n for n in range(5)]
# for func in funclist:
#     print(func(0))
##################################
# partical回调参数
# def output_result(result, log=None):
#     if log is not None:
#         log.debug('Got: %r', result)


# # A sample function
# def add(x, y):
#     return x + y


# if __name__ == '__main__':
#     import logging
#     from functools import partial
#     from multiprocessing import Pool

#     logging.basicConfig(level=logging.DEBUG)
#     log = logging.getLogger('test')

#     p = Pool()
#     # multiprocessing仅仅只是使用单个值来调用回调函数，所以要partical一下。
#     p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
#     p.close()
#     p.join()
#############################################
# # partial增加第三方类实例的属性
# from functools import partial
# from socketserver import StreamRequestHandler, TCPServer


# class EchoHandler(StreamRequestHandler):
#     # 重写init,增加一个必传的ack强制关键字
#     def __init__(self, *args, ack, **kwargs):
#         self.ack = ack
#         super().__init__(*args, **kwargs)

#     def handle(self):
#         for line in self.rfile:
#             self.wfile.write(b'GOT:' + line)


# serv = TCPServer(('', 15000), partial(EchoHandler, ack=b"RECIEVED:"))
# serv.serve_forever()
######################
# # 回调函数获取信息
# def apply_async(func, *args, callback):
#     # Compute the result
#     result = func(*args)

#     # Invoke the callback with the result
#     callback(result)


# # def print_result(result):
# #     print('Got:', result)


# # # 注意到 回调print_result() 函数仅仅只接受一个参数 result 。不能再传入其他信息。
# # apply_async(sum, (2, 3), callback=print_result)

# # # 为了让回调函数访问外部信息，一种方法是使用类储存信息(方法可以获取内部的state)。
# # # 第二种方式，作为类的替代，可以使用一个闭包捕获状态值(useState钩子)。
# # def handler_wrapper():
# #     state = 0

# #     def handler(result):
# #         # 注意：不加nonlocal则不是闭包
# #         # state = 0
# #         nonlocal state
# #         state += 1
# #         print('[{}] Got: {}'.format(state, result))

# #     return handler


# # handler = handler_wrapper()
# # apply_async(sum, (2, 3), callback=handler)
# # apply_async(sum, (2, 3), callback=handler)

# # 还有另外一个更高级的方法，可以使用协程来完成同样的事情：
# def make_handler():
#     sequence = 0
#     while True:
#         result = yield
#         sequence += 1
#         print('[{}] Got: {}'.format(sequence, result))


# handler = make_handler()

# # 激活生成器
# next(handler)
# apply_async(sum, (2, 3), callback=handler.send)

##############
print([(i, j) for i in range(3) for j in range(i)])
print(list(enumerate(["a", "b", "c"], start=2)))
# isinstance可以接收一个元组¶
print(isinstance("1.3", (float, int, str)))