"""
This is a c9 doc
"""
print('package:' + (__package__ or '当前模块不属于任何包'))
print('name:' + __name__)
print('doc:' + (__doc__ or '当前模块没有文档注释'))
print('file:' + __file__)
