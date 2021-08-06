# 这段代码可以做任何更高级的处理，包括线程、进程和定时器，但是这些都不是我们要关心的
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

# 注意到 print_result() 函数仅仅只接受一个参数 result 。不能再传入其他信息。
# 而当你想让回调函数访问其他变量或者特定环境的变量值的时候就会遇到麻烦。
def print_result(result):
    print("Got:", result)


apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('hello', 'world'), callback=print_result)
