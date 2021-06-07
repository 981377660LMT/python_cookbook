import threading

# 条件变量， 用于复杂的线程间同步
# class XiaoAi(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="小爱")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{} : 在 ".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{} : 好啊 ".format(self.name))
#         self.lock.release()
#
# class TianMao(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="天猫精灵")
#         self.lock = lock
#
#     def run(self):
#
#         self.lock.acquire()
#         print("{} : 小爱同学 ".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{} : 我们来对古诗吧 ".format(self.name))
#         self.lock.release()

# 通过condition完成协同读诗


class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        # acquire获得Condition对象的锁
        # Condition对象的构造函数可以接受一个Lock/RLock对象作为参数，如果没有指定，则Condition对象会在内部自行创建一个RLock
        with self.cond:
            # 调用wait方法时，线程会释放Condition内部的锁并进入blocked状态，同时在waiting池中记录这个线程
            self.cond.wait()
            print("{} : 在 ".format(self.name))
            # 当调用notify方法时，Condition对象会从waiting池中挑选一个线程，通知其调用acquire方法尝试取到锁
            # 处于waiting池的线程只能通过notify方法唤醒
            self.cond.notify()

            self.cond.wait()
            print("{} : 好啊 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 君住长江尾 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 共饮长江水 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 此恨何时已 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 定不负相思意 ".format(self.name))
            self.cond.notify()


class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        with self.cond:
            print("{} : 小爱同学 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 我们来对古诗吧 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 我住长江头 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 日日思君不见君 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 此水几时休 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 只愿君心似我心 ".format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == "__main__":
    # from concurrent import futures

    cond = threading.Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    # 启动顺序很重要
    # 在调用with cond之后才能调用wait或者notify方法
    # condition有两层锁， 一把底层锁会在线程调用了wait方法的时候释放， 上面的锁会在每次调用wait的时候分配一把并放入到cond的等待队列中，等到notify方法的唤醒
    xiaoai.start()
    tianmao.start()
