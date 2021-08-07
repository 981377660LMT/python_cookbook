from queue import Queue
from threading import Thread
import time

# 从一个线程向另一个线程发送数据最安全的方式可能就是使用 queue 库中的队列了
# 当使用队列时，协调生产者和消费者的关闭问题可能会有一些麻烦。一个通用的解决方法是在队列中放置一个特殊的值，当消费者读到这个值的时候，终止执行
_sentinel = object()

# A thread that produces data
def producer(out_q):
    n = 10
    while n > 0:
        # Produce some data
        out_q.put(n)
        time.sleep(2)
        n -= 1

    # Put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()

        # Check for termination
        # 消费者在读到这个特殊值之后立即又把它放回到队列中，将之传递下去
        # 这样，所有监听这个队列的消费者线程就可以全部关闭了
        if data is _sentinel:
            in_q.put(_sentinel)
            break

        # Process the data
        print('Got:', data)
    print('Consumer shutting down')


if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

