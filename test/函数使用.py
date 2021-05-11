# # format_map的参数不需传入“关键字=真实值”，而是直接传入真实的字典值。我们来看个案例：
# student = {'name': '小明', 'class': '20190301', 'score': 597.5}
# s1 = '{st[class]}班{st[name]}总分：{st[score]}'.format(st=student)
# s2 = '{class}班{name}总分：{score}'.format_map(student)
#####
# 协程
def simple_coroutine():
    print('-> start')
    x = yield 1
    print('-> recived', x)


sc = simple_coroutine()

print(sc.__next__())
# 调用send方法，把值传给 yield 的变量，然后协程恢复，继续执行下面的代码，直到运行到下一个 yield 表达式，或者终止。
sc.send('zhexiao')
