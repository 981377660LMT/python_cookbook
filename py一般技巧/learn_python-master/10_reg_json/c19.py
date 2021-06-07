import re

# json_str = "{name:qiyue, age:18}"
# r = re.findall('{name:(.+), age:(.+)}', json_str)
# print(r)

import json

# JSON规定字符串必须是双引号，key必须是字符串
# 字符串 -> 数据结构，叫反序列化
json_str = '{"name":"qiyue", "age":18}'
student = json.loads(json_str)
print(type(student))
print(student)
print(student['name'])
print(student['age'])

json_str = '[{"name":"qiyue", "age":18, "Flag":false}, {"name":"qiyue2", "age":19}]'
students = json.loads(json_str)
print(type(students))
print(students)

# json      python
# object    dict
# array     list
# string    str
# number    int
# number    float
# true      True
# false     False
# null      None
