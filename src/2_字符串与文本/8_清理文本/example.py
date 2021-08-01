# example.py
#
# Example of some tricky sanitization problems

# A tricky string
s = 'p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n'
print(s)

# 第一步是清理空白字符
# (a) Remapping whitespace
# 空白字符 \t 和 \f 已经被重新映射到一个空格。回车字符r直接被删除
remap = {ord('\t'): ' ', ord('\f'): ' ', ord('\r'): None}  # Deleted

a = s.translate(remap)
print('whitespace remapped:', a)

# 让我们删除所有的和音符
# (b) Remove all combining characters/marks
import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
#  将862个和音符变为Node
# 通过使用 dict.fromkeys() 方法构造一个字典，每个Unicode和音符作为键，对应的值全部为 None 。
c = b.translate(cmb_chrs)
print('accents removed:', c)
##################################################
# (c) Accent removal using I/O decoding
d = b.encode('ascii', 'ignore').decode('ascii')
print('accents removed via I/O:', d)

# 清理空白字符
def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s