# 状态模式入门
# 实现一个状态机或者是在不同状态下执行操作的对象，但是又不想在代码中出现太多的条件判断语句。
# class Connection:
#     """读写开关:普通方案，好多个判断语句，效率低下~~"""

#     def __init__(self):
#         self.state = 'CLOSED'

#     def read(self):
#         if self.state != 'OPEN':
#             raise RuntimeError('Not open')
#         print('reading')

#     def write(self, data):
#         if self.state != 'OPEN':
#             raise RuntimeError('Not open')
#         print('writing')

#     def open(self):
#         if self.state == 'OPEN':
#             raise RuntimeError('Already open')
#         self.state = 'OPEN'

#     def close(self):
#         if self.state == 'CLOSED':
#             raise RuntimeError('Already closed')
#         self.state = 'CLOSED'

# 这里的解决方案是将每个状态抽取出来定义成一个类。
from abc import ABCMeta, abstractmethod


class Connection:
    """新方案——对每个状态(关闭,打开)定义一个类"""

    def __init__(self):
        self.set_state(ClosedConnectionState)

    def set_state(self, newstate):
        self._state = newstate
        # Delegate to the state class

    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)


# 接口
class IConnectionState(metaclass=ABCMeta):
    @abstractmethod
    def read(conn):
        raise NotImplementedError()

    @abstractmethod
    def write(conn, data):
        raise NotImplementedError()

    @abstractmethod
    def open(conn):
        raise NotImplementedError()

    @abstractmethod
    def close(conn):
        raise NotImplementedError()


# Implementation of different states
class ClosedConnectionState(IConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')

    @staticmethod
    def open(conn):
        conn.set_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')


class OpenConnectionState(IConnectionState):
    @staticmethod
    def read(conn):
        print('reading')

    @staticmethod
    def write(conn, data):
        print('writing')

    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')

    @staticmethod
    def close(conn):
        conn.set_state(ClosedConnectionState)


c = Connection()
print(c._state)
c.open()
c.write('hello')
c.close()

# 这里看上去有点奇怪，每个状态对象都只有静态方法，并没有存储任何的实例属性数据。
# 实际上，所有状态信息都只存储在 Connection 实例中。