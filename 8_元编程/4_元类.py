# 元类是创建类的东西
def say(self):
    return "i am user"
    # return self.name


Base = type("User", (object,), {'name': 'cmnx', 'say': say})


User = type("User", (Base,), {})


class MetaClassShouldExtendsType(type):
    def __new__(cls, *args, **kwargs):
        # 也即type.__new__(cls, name, bases, attrs)
        return super().__new__(cls, *args, **kwargs)


class MetaUser(metaclass=MetaClassShouldExtendsType):
    pass


user = User()

print(user.name, user.say())
