from inspect import Signature, Parameter


parms = [
    Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
    Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
    Parameter('z', Parameter.KEYWORD_ONLY, default=None,),
]
# 1. 创建签名对象
sig = Signature(parms)
assert str(sig) == '(x, y=42, *, z=None)'

# 2. 使用它的 bind() 方法很容易的将它绑定到 *args 和 **kwargs 上去
def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)

func(1, z=3)