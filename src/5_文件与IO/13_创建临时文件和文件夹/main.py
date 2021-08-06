# 尽可能以最安全的方式使用 tempfile 模块来创建临时文件
# TemporaryFile() 、NamedTemporaryFile() 和 TemporaryDirectory() 函数
# 应该是处理临时文件目录的最简单的方式了，因为它们会自动处理所有的创建和清理步骤
from tempfile import NamedTemporaryFile
from tempfile import TemporaryDirectory

with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)
    # Use the directory
    ...
# Directory and all contents destroyed

with NamedTemporaryFile('w+t', encoding='utf-8', delete=True) as f:
    print('filename is:', f.name)
    ...

# File automatically destroyed
# 和 TemporaryFile() 一样，结果文件关闭时会被自动删除掉。 如果你不想这么做，可以传递一个关键字参数 delete=False 即可
