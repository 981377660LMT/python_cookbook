import os.path


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        # readinto() 填充已存在的缓冲区而不是为新对象重新分配内存再返回它们
        # 使用 f.readinto() 时需要注意的是，你必须检查它的返回值，也就是实际读取的字节数。
        f.readinto(buf)
    return buf


with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')


buf = read_into_buffer('sample.bin')

print(buf[0:5])

with open('newsample.bin', 'wb') as nf:
    nf.write(buf)
