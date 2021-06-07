"""
a source syndicates events/data to 0+ registered listeners 
"""

# 书店
class BookProvider:
    def __init__(self):
        # 来源于Publisher的book
        self.book = []
        self.subscribers = {}

    def notify(self, book):
        self.book.append(book)

    # 登记书的订阅人数
    def subscribe(self, book, subscriber):
        self.subscribers.setdefault(book, []).append(subscriber)

    def unsubscribe(self, book, subscriber):
        self.subscribers[book].remove(subscriber)

    # 发布所有书
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


message_center = BookProvider()
fftv = Publisher(message_center)
jim = Subscriber("jim", message_center)
jim.subscribe("cartoon")
fftv.publish("cartoon")
message_center.update()
