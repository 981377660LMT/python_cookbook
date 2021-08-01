import os

filenames = os.listdir('.')

# 将所有的匹配项放入到一个元组中去， 然后传给 startswith() 或者 endswith() 方法
foo = [file for file in filenames if file.endswith(('.py', '.md'))]
print(foo)
