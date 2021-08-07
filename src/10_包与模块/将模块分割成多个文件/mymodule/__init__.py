# __init__.py

from .a import A
from .b import B


# 组件在需要时被加载
def A():
    from .a import A

    return A()


def B():
    from .b import B

    return B()
