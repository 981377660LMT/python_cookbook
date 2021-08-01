import sys

s = '{name} has {n} messages'
# print(s.format(name="A", n=2))

# 如果要被替换的变量能在变量域中找到， 那么你可以结合使用 format_map() 和 vars()
name = "A"
n = 2
print(vars())
print(s.format_map(vars()))

# vars():
# Without arguments, equivalent to locals(). With an argument, equivalent to object.__dict__.

# format 和 format_map() 的一个缺陷就是它们并不能很好的处理变量缺失的情况


class safesub(dict):
    """"防止keyError"""

    def __missing__(self, key):
        return f'{key}'


del n
print(s.format_map(safesub(vars())))

# 变量替换步骤用一个工具函数封装起来。就像下面这样：

# sub() 函数使用 sys._getframe(1) 返回调用者的栈帧。可以从中访问属性 f_locals 来获得局部变量。
# 值得注意的是 f_locals 是一个复制调用函数的本地变量的字典。 尽管你可以改变 f_locals 的内容，但是这个修改对于后面的变量访问没有任何影响。
def sub(text):
    print(sys._getframe(1).f_locals)
    return text.format_map(safesub(sys._getframe(1).f_locals))


print(sub('hello {namea}'))
