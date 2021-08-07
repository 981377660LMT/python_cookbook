# class Foo(object):
#     bar = True
# Can be translated to:

# Object.create({}, { p: { value: 42 } })
Foo = type('Foo', (), {'bar': True})

print(Foo.__mro__)

