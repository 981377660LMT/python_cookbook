# 扩展函数中的某个闭包，允许它能像类实例一样，访问和修改函数的内部变量。
# 编写访问函数并将其作为函数属性绑定到闭包上来实现这个目的。
def sample():
    n = 0

    # Closure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func


# foo有点像类实例了
foo = sample()
foo()
foo.set_n(2)
print(foo.get_n())
