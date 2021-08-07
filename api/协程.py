# https://blog.csdn.net/andybegin/article/details/77884645?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522162070045616780255233547%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=162070045616780255233547&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-77884645.first_rank_v2_pc_rank_v29&utm_term=%E5%8D%8F%E7%A8%8B+python
# def averager():
#     total = 0.0
#     count = 0
#     avg = None

#     while True:
#         num = yield avg
#         total += num
#         count += 1
#         avg = total / count


# # run
# ag = averager()
# # 预激协程
# print(next(ag))  # None

# print(ag.send(10))  # 10
# print(ag.send(20))  # 15
# 终止协程和异常处理
class DemoException(Exception):
    """
    custom exception
    """


def handle_exception():
    print('-> start')

    while True:
        try:
            x = yield
        except DemoException:
            print('-> run demo exception')
        else:
            print('-> recived x:', x)

    raise RuntimeError('this line should never run')


he = handle_exception()
next(he)
he.send(10)  # recived x: 10
he.send(20)  # recived x: 20

he.throw(DemoException)  # run demo exception

he.send(40)  # recived x: 40
he.close()

# send表示传入变量至yield左侧然后向下开始下一次yield