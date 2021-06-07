import seven.t.c7 as m
print(m.a)

from seven.t.c7 import a
print(a)

from seven.t import c7

print(c7.a)

from seven.t.c7 import *
print(a)
print(c)
# print(d)
