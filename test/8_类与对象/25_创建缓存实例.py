# 相同参数创建的对象时单例的;

# 编写一个工厂函数来修改普通的实例创建行为通常是一个比较简单的方法。
# Caching support
import weakref

# _spam_cache = weakref.WeakValueDictionary()

# # The class in question
# class Spam:
#     def __init__(self, name):
#         self.name = name


# def get_spam(name):
#     if name not in _spam_cache:
#         s = Spam(name)
#         _spam_cache[name] = s
#     else:
#         s = _spam_cache[name]
#     return s


# a = get_spam('foo')
# b = get_spam('bar')
# print(a is b)

# c = get_spam('foo')
# print(a is c)
######################################
# ------------------------最后的修正方案------------------------
class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            temp = Spam._new(name)  # Modified creation
            self._cache[name] = temp
        else:
            temp = self._cache[name]
        return temp

    def clear(self):
        self._cache.clear()


class Spam:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")

    # Alternate constructor
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self


s = Spam._new('a')
print(s)
