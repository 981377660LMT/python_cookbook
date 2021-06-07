""""
The Decorator pattern is used to dynamically add a new feature to an
object without changing its implementation.
It differs from inheritance because the new feature is added only to that particular
object, not to the entire subclass.
装饰器模式用于动态添加新功能到对象而不改变其实现。
它不同于继承，因为新功能仅添加到该特定对象，而不是整个子类。
"""


class TextTag:
    """Represents a base text tag"""

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<b>{self._wrapped.render()}</b>"


class ItalicWrapper(TextTag):
    """Wraps a tag in <i>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<i>{self._wrapped.render()}</i>"


if __name__ == '__main__':
    simple_hello = TextTag("hello, world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))

    print("before:", simple_hello.render())

    print("after:", special_hello.render())
