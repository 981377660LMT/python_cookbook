class ObjectPool:
    def __init__(self, queue, auto_get=False) -> None:
        self._queue = queue
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, type, value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __delete__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None


if __name__ == '__main__':
    import queue

    q = queue.Queue()
    q.put("yam")
    with ObjectPool(q) as obj:
        print(obj)

    print('Outside with: {}'.format(q.get()))

    q.put("sam")
    pool = ObjectPool(q, True)
    print('Inside func: {}'.format(pool.item))

