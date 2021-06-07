"""
keep track of all subclasses of a given class  
元类追跡子类：ORM
"""


class RegistryHolder(type):
    REGISTRY = {}

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        # 保存子类信息
        cls.REGISTRY[new_cls.__name__] = new_cls
        return new_cls

    @classmethod
    def get_registry(cls):
        return dict(cls.REGISTRY)


class BaseRegisteredClass(metaclass=RegistryHolder):
    """
    Any class that will inherits from BaseRegisteredClass will be included
    inside the dict RegistryHolder.REGISTRY, the key being the name of the
    class and the associated value, the class itself.
    从 BaseRegisteredClass 继承的任何类将
    在字典 RegistryHolder.REGISTRY 中被注册，键是
    类和关联的值，即类本身。
    """


print(sorted(RegistryHolder.REGISTRY))

