import re

text2 = '''/* this is a
multiline comment */
'''

# re.DOTALL可以让正则表达式中的点(.)匹配包括换行符在内的任意字符
regexp = re.compile(r"/\*(.*?)\*/", flags=re.DOTALL)

print(regexp.findall(text2))
