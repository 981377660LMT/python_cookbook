""""
此模式旨在减少所需的类数。它不依赖于子类，而是在运行时复制原型实例 
创建对象。
当实例化类很昂贵时使用。
Creates new object instances by cloning prototype.
"""
from typing import Any, Dict


class Prototype:
    def __init__(self, value: str = "default", **attrs: Dict[str, Any]) -> None:
        self.value = value
        self.__dict__.update(attrs)

    # 拷贝并更新原型
    def clone(self, **attrs: Any):
        obj = self.__class__(**self.__dict__)
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher:
    def __init__(self):
        self._objects = {}

    def get_objects(self) -> Dict[str, Prototype]:
        """Get all objects"""
        return self._objects

    def register_object(self, name: str, obj: Prototype) -> None:
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name: str) -> None:
        """Unregister an object"""
        del self._objects[name]


if __name__ == '__main__':
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    d = prototype.clone()
    a = prototype.clone(value="as", cc="as")
    b = a.clone(value='b-value', is_checked=True)

    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)

    print([{n: p.value} for n, p in dispatcher.get_objects().items()])
