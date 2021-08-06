# 相同参数创建的对象时单例的;
# 为了达到这样的效果，你需要使用一个和类本身分开的工厂函数
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
# 我们还能否找到更优雅的解决方案呢？
# 一个 WeakValueDictionary 实例只会保存那些在其它地方还在被使用的实例
#  否则的话，只要实例不再被使用了，它就从字典中被移除了。
# ------------------------最后的修正方案------------------------
# 将缓存代码放到一个单独的缓存管理器中
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
    manager = CachedSpamManager()

    # 将构造函数私有的思路;需要使用工厂方法创建对象
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")

    # Alternate constructor
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self

    @classmethod
    def get_spam(cls, name):
        return cls.manager.get_spam(name)


s = Spam.get_spam('a')
Spam.get_spam('a')

print(s)

#  缓存和其他构造模式还可以使用9.13小节中的元类实现的更优雅一点
