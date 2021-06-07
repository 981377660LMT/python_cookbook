"""
Reference:
http://www.slideshare.net/ishraqabd/publish-subscribe-model-overview-13368808
Author: https://github.com/HanWenfang
"""
from typing import TypeVar


# 书店
class BookProvider:
    def __init__(self):
        self.book = []
        self.subscribers = {}

    def notify(self, book):
        self.book.append(book)

    # 登记书的订阅人数
    def subscribe(self, book, subscriber):
        self.subscribers.setdefault(book, []).append(subscriber)

    def unsubscribe(self, book, subscriber):
        self.subscribers[book].remove(subscriber)

    def update(self):
        for book in self.book:
            for sub in self.subscribers.get(book, []):
                sub.run(book)
        self.book = []


# 出版社
class Publisher:
    def __init__(self, book_center: BookProvider):
        self.provider = book_center

    def publish(self, book):
        self.provider.notify(book)


# 订阅者
class Subscriber:
    def __init__(self, name, msg_center):
        self.name = name
        self.provider = msg_center

    def subscribe(self, book):
        self.provider.subscribe(book, self)

    def unsubscribe(self, book):
        self.provider.unsubscribe(book, self)

    def run(self, book):
        print(f"{self.name} got {book}")


def main():
    """
    >>> message_center = BookProvider()

    >>> fftv = Publisher(message_center)

    >>> jim = Subscriber("jim", message_center)
    >>> jim.subscribe("cartoon")
    >>> jack = Subscriber("jack", message_center)
    >>> jack.subscribe("music")
    >>> gee = Subscriber("gee", message_center)
    >>> gee.subscribe("movie")
    >>> vani = Subscriber("vani", message_center)
    >>> vani.subscribe("movie")
    >>> vani.unsubscribe("movie")

    # Note that no one subscribed to `ads`
    # and that vani changed their mind

    >>> fftv.publish("cartoon")
    >>> fftv.publish("music")
    >>> fftv.publish("ads")
    >>> fftv.publish("movie")
    >>> fftv.publish("cartoon")
    >>> fftv.publish("cartoon")
    >>> fftv.publish("movie")
    >>> fftv.publish("blank")

    >>> message_center.update()
    jim got cartoon
    jack got music
    gee got movie
    jim got cartoon
    jim got cartoon
    gee got movie
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
