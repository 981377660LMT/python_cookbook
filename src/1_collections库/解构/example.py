# example.py
#
# Unpacking of tagged tuples of varying sizes
# 星号表达式在迭代元素为可变长元组的序列时是很有用的。
'''
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for (tag, *args) in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
'''
# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *_, homedir, sh = line.split(':')
print(homedir)


# 解构语法去巧妙的实现递归算法
def sum(li):
    head, *tail = li
    return head+sum(tail) if tail else head


print(sum([1, 2, 3, 4, 5]))
