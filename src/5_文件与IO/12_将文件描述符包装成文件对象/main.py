# 一个文件描述符(fd)和一个打开的普通文件(f)是不一样的
# 文件描述符仅仅是一个由操作系统指定的整数，用来指代某个系统的I/O通道。
# 如果你碰巧有这么一个文件描述符，你可以通过使用 open() 函数来将其包装为一个Python的文件对象
# 你仅仅只需要使用这个整数值的文件描述符作为第一个参数来代替文件名即可
import os

# Open a low-level file descriptor
fd = os.open('fd.py', os.O_WRONLY | os.O_CREAT)

# Turn into a proper file
f = open(fd, 'wt')

f.write('okey dokey')
f.close()
# 当高层的文件对象被关闭或者破坏的时候，底层的文件描述符也会被关闭
# 在Unix系统中，这种包装文件描述符的技术可以很方便的将一个类文件接口作用于一个以不同方式打开的I/O通道上， 如管道、套接字等
