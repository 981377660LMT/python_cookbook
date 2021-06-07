from copy import copy, deepcopy


# 使用闭包存储obj，
# foo=memento(obj),以后出错时调用foo()就回到原来存储时的状态
def memento(obj, deep=False):
    state = deepcopy(obj.__dict__) if deep else copy(obj.__dict__)

    def restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)

    return restore


class Transaction:
    """A transaction guard.

    This is, in fact, just syntactic sugar around a memento closure.
    """

    deep = False
    states = []

    def __init__(self, deep, *targets):
        self.deep = deep
        self.targets = targets
        self.commit()

    # 保存target的状态至states
    def commit(self):
        self.states = [memento(target, self.deep) for target in self.targets]

    # 每个target全部回到出错前的状态
    def rollback(self):
        for a_state in self.states:
            a_state()


class Transactional:
    """Adds transactional semantics to methods. Methods decorated  with

    @Transactional will rollback to entry-state upon exceptions.
    """

    def __init__(self, method):
        self.method = method

    # 这里不如上下文管理器实现
    def __get__(self, obj, T):
        def transaction(*args, **kwargs):
            state = memento(obj)
            try:
                return self.method(obj, *args, **kwargs)
            except Exception as e:
                state()
                raise e

        return transaction


class NumObj:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.value!r}>"

    def increment(self):
        self.value += 1

    @Transactional
    def do_stuff(self):
        self.value = "1111"  # <- invalid value
        self.increment()  # <- will fail and rollback


if __name__ == '__main__':
    num_obj = NumObj(-1)

    print(num_obj)
    a_transaction = Transaction(True, num_obj)
    try:
        for i in range(3):
            num_obj.increment()
            print(num_obj)
        a_transaction.commit()
        print('-- committed')
        for i in range(3):
            num_obj.increment()
            print(num_obj)
        num_obj.value += 'x'  # will fail
        print(num_obj)
    except Exception:
        a_transaction.rollback()
        print('-- rolled back')
    print(num_obj)

    try:
        num_obj.do_stuff()
    except Exception:
        print('-> doing stuff failed!')
        import sys
        import traceback

        traceback.print_exc(file=sys.stdout)
    print(num_obj)

# 不如上下文管理器
