from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        print(sig.parameters, 6666)
        # 部分绑定要检查的属性类型
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
        print(bound_types, 'bt')

        @wraps(func)
        def wrapper(*args, **kwargs):
            # sig.bind()不允许忽略任何参数
            bound_values = sig.bind(*args, **kwargs)
            print(bound_values, 'bv')
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))
            return func(*args, **kwargs)

        return wrapper

    return decorate


# Examples


@typeassert(int, int)
def add(x, y):
    return x + y


@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)


if __name__ == '__main__':
    print(add(2, 3))
    try:
        add(2, 'hello')
    except TypeError as e:
        print(e)

    spam(1, 2, 3)
    spam(1, 'hello', 3)
    try:
        spam(1, 'hello', 'world')
    except TypeError as e:
        print(e)


# inspect.signature() 函数。 简单来讲，它运行你提取一个可调用对象的参数签名信息。

# bind_partial() 方法来执行从指定类型到名称的部分绑定。

