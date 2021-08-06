# 文件名的匹配，你可能会考虑使用 glob 或 fnmatch 模块
import os
import os.path
import glob

pyfiles = glob.glob('*.py')
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles]

for name, size, mtime in name_sz_date:
    print(name, size, mtime)
#  其实可以直接用
# #  os.walk()