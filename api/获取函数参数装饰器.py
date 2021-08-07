from functools import wraps


def test(func):
    print(func.__name__)

    # 获取函数传参
    # 在ts里需要获取descriptor.value才能获取函数传参
    # @wraps(func)保持函数元信息
    @wraps(func)
    def wrapper(*args):
        print('参数', *args)
        result = func(*args)
        return result

    return wrapper


@test
def foo(a, b):
    print('bar')
    return 'test'


print(foo(1, 2))
