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
# partial增加第三方类实例的属性
from functools import partial
from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    # 重写init,增加一个必传的ack强制关键字
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(b'GOT:' + line)


serv = TCPServer(('', 15000), partial(EchoHandler, ack=b"RECIEVED:"))
serv.serve_forever()