# gzip 和 bz2 模块可以很容易的处理这些文件

import gzip
import bz2

text = 'qwertyuiop'
# gzip compression
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

# bz2 compression

with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)
