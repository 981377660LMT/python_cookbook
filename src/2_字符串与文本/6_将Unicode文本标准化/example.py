# example.py
#
# Example of unicode normalization
# 在Unicode中，某些字符能够用多个合法的编码表示
#  为了修正这个问题，你可以使用unicodedata模块先将文本标准化：
# Two strings
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

# (a) Print them out (usually looks identical)
print(s1)
print(s2)

# (b) Examine equality and length
print('s1 == s2', s1 == s2)
print(len(s1), len(s2))
###########################################
# (c) Normalize and try the same experiment
import unicodedata

# NFC表示字符应该是整体组成(比如可能的话就使用单一编码)，而NFD表示字符应该分解为多个组合字符表示。
n_s1 = unicodedata.normalize('NFC', s1)
n_s2 = unicodedata.normalize('NFC', s2)

print('n_s1 == n_s2', n_s1 == n_s2)
print(len(n_s1), len(n_s2))

# (d) Example of normalizing to a decomposed form and stripping accents
t1 = unicodedata.normalize('NFD', s1)
# combining() 函数可以测试一个字符是否为和音字符
print(''.join(c for c in t1 if not unicodedata.combining(c)))
