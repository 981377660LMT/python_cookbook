import time
import threading
import pickle

# 如果定义了这两个方法，pickle.dump() 就会调用 __getstate__()
# 获取序列化的对象。
# 类似的，__setstate__() 在反序列化时被调用


class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)


c = Countdown(30)
with open('state.p', 'wb') as f:
    pickle.dump(c, f)

with open('state.p', 'rb') as f:
    pickle.load(f)

# 由于 pickle 是Python特有的并且附着在源码上，所有如果需要长期存储数据的时候不应该选用它
# 对于在数据库和存档文件中存储数据时，你最好使用更加标准的数据编码格式如XML，CSV或JSON。
# 这些编码格式更标准，可以被不同的语言支持，并且也能很好的适应源码变更。
