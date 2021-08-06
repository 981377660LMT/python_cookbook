import time
from contextlib import contextmanager

# yield 之前的代码会在上下文管理器中作为 __enter__() 方法执行，
# 所有在 yield 之后的代码会作为 __exit__() 方法执行。
@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


# Example use
with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1
