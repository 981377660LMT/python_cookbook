# Some examples of reading text files with different options
#
# The file sample.txt is a UTF-8 encoded text file with Windows
# line-endings (\r\n).

# (a) Reading a basic text file (UTF-8 default encoding)

#  t 表示文本模式，这意味着在写入文件时将 open() 个字符转换为主机OS行结尾，并在读取时再次返回
# 默认t 另外一种是二进制模式b

# 关于换行符的识别问题，在Unix和Windows中是不一样的(分别是 \n 和 \r\n )。
# 默认情况下，Python会以统一模式处理换行符。 这种模式下，在读取文本的时候，Python可以识别所有的普通换行符并将其转换为单个 \n 字符


print("Reading a simple text file (UTF-8)")
with open('sample.txt', 'rt') as f:
    for line in f:
        print(repr(line))

# (b) Reading a text file with universal newlines turned off
print("Reading text file with universal newlines off")
# newline = ''会将换行符 \n 转换为系统默认的换行符
with open('sample.txt', 'rt', newline='') as f:
    for line in f:
        print(repr(line))

# (c) Reading text file as ASCII with replacement error handling
print("Reading text as ASCII with replacement error handling")
with open('sample.txt', 'rt', encoding='ascii', errors='replace') as f:
    for line in f:
        print(repr(line))

# (d) Reading text file as ASCII with ignore error handling
print("Reading text as ASCII with ignore error handling")
with open('sample.txt', 'rt', encoding='ascii', errors='ignore') as f:
    for line in f:
        print(repr(line))

