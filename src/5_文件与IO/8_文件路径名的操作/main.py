from genericpath import isfile
from os.path import (
    dirname,
    basename,
    join,
    exists,
    expanduser,
    splitext,
    isfile,
    islink,
    isdir,
    getsize,
    getmtime,
)

path = '~/Data/data.csv'
print(expanduser(path))
print(splitext(path))

extname = splitext(path)[1]
print(extname)
# os.path 模块知道Unix和Windows系统之间的差异并且能够可靠地处理类似 Data/data.csv 和 Data\data.csv 这样的文件名。
#  os.path 来进行文件测试是很简单的。 在写这些脚本时，可能唯一需要注意的就是你需要考虑文件权限的问题
# PermissionError
