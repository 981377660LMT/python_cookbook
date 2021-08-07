# Example of making a class manually from parts
# 使用函数 types.new_class() 来初始化新的类对象

# Methods
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    '__init__': __init__,
    'cost': cost,
}

# Make a class
import types

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__

if __name__ == '__main__':
    s = Stock('ACME', 50, 91.1)
    print(s)
    print(s.cost())
