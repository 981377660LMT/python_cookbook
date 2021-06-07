import re
language = 'PythonC#JavaPHP'
# re.I让正则表达式匹配忽略大小写，多个模式使用|分隔
r = re.findall('c#', language, re.I | re.S)
print(r)

# 默认.不匹配\n，re.S使.能够匹配\n
language = 'PythonC#\nJavaPHP'
r = re.findall('c#.{1}', language, re.I | re.S)
print(r)
