# -*- coding: utf-8 -*-


class LowerCaseMeta(type):
    def __new__(cls, name, bases, attrs):
        lower_attrs = {}
        for k, v in attrs.items():
            if not k.startswith('__'):
                lower_attrs[k.lower()] = v
            else:
                lower_attrs[k] = v
        return type.__new__(cls, name, bases, lower_attrs)


class Foo(metaclass=LowerCaseMeta):
    BB = True

    def HELLO(self):
        print('hello')


print(dir(Foo))
