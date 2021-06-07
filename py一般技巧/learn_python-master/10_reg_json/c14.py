import re
language = 'PythonC#JavaC#PHPC#'
# 正则替换
# 第一个参数是被替换参数
# 第二个参数是要替换字符串
# 第三个参数是原始字符串
# count指，0表示永远替换下去，1表示只替换第一个
# r = re.sub('C#', 'GO', language, 0)
# print(r)

# 也可以用python内置的replace函数实现字符串替换
# language = language.replace('C#', 'GO')
# print(language)


def convert(value):
    # print(value)
    matched = value.group()
    return '!!' + matched + '!!'


# sub的要替换字符串也可以是函数
r = re.sub('C#', convert, language)
print(r)
