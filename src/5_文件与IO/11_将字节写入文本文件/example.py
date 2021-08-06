# Example of writing raw bytes on a file opened in text mode
# 通过读取文本文件的 buffer 属性来读取二进制数据
import sys

# A byte string
data2 = 'Hello World\n'
data = b'Hello World\n'

# Write onto the buffer attribute (bypassing text encoding)
sys.stdout.write(data2)
sys.stdout.buffer.write(data)

# print(data)

# I/O系统以层级结构的形式构建而成。
# 文本文件是通过在一个拥有缓冲的二进制模式文件上增加一个Unicode编码/解码层来创建
# buffer 属性指向对应的底层文件。如果你直接访问它的话就会绕过文本编码/解码层
