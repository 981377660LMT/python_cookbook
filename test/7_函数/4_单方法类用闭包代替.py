from urllib.request import urlopen

# 大部分情况下，你拥有一个单方法类的原因是需要存储某些额外的状态来给方法使用。
# 比如，定义UrlTemplate类的唯一目的就是先在某个地方存储模板值，以便将来可以在open()方法中使用。
class UrlTemplate:
    def __init__(self, template: str) -> None:
        self.template = template

    def open(self, **kwargs):
        # format_map的参数不需传入“关键字=真实值”，而是直接传入真实的字典值。我们来看个案例：
        # 切片，字典映射都是getitem的操作
        return urlopen(self.template.format_map(kwargs))


yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))

# 使用一个内部函数或者闭包的方案通常会更优雅一些。
# 简单来讲，一个闭包就是一个函数， 只不过在函数内部带上了一个额外的变量环境。
# 闭包关键特点就是它会记住自己被定义时的环境。
# 因此，在我们的解决方案中，opener() 函数记住了 template 参数的值，并在接下来的调用中使用它。
def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))