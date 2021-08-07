# dis 模块可以被用来输出任何Python函数的反编译结果。
import dis
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('Blastoff!')

print(dis.dis(countdown))