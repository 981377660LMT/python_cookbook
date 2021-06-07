""""
In Python, instance attributes are stored in a
attribute dictionary called __dict__.
Usually, each instance will have
its own dictionary, but the Borg pattern modifies this so that all
instances have the same dictionary.

*Where is the pattern used practically?
Sharing state is useful in applications like managing database connections
数据库连接
"""


class Singleton:
    _shared_state = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared_state


class YourBorg(Singleton):
    def __init__(self, state=None) -> None:
        super().__init__()
        if state:
            self.state = state
        else:
            if not hasattr(self, "state"):
                self.state = "Init"

    def __str__(self) -> str:
        return self.state


if __name__ == '__main__':
    foo = YourBorg()
    print(foo)
    foo1 = YourBorg("as")
    print(foo, foo1)
    foo2 = YourBorg()
    print(foo, foo1, foo2)
    foo3 = YourBorg("aaa")
    for i in [foo, foo1, foo2, foo3]:
        print(i)

