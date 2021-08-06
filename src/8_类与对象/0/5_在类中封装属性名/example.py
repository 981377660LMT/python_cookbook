# Example of using __ method name to implement a
# non-overrideable method

# 第一个约定是任何以单下划线_开头的名字都应该是内部实现
# 使用双下划线开始会导致访问名称变成其他形式。
# 到底哪种方式好呢？
# 大多数而言，你应该让你的非公共名称以单下划线开头。
# 但是，如果你清楚你的代码会涉及到子类，
# 并且有些内部属性应该在子类中隐藏起来，
# 那么才考虑使用双下划线方案。
# 还有一点要注意的是，有时候你定义的一个变量和某个保留关键字冲突，这时候可以使用单下划线作为后缀
lambda_ = 2.0


class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        print('B.__private_method', self.__private)

    def public_method(self):
        self.__private_method()


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1  # Does not override B.__private

    # Does not override B.__private_method()
    def __private_method(self):
        print('C.__private_method')


c = C()
c.public_method()

