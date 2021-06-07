# 全局变量
c = 10


def demo():
    # 局部变量
    c = 50
    print(c)
    for i in range(0, 9):
        a = 'a'
        c += 1
    print(c)
    # 在for循环外部可以引用for循环里面的变量
    # 因为Python没有块级作用域概念
    print(a)


demo()
