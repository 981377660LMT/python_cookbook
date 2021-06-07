import seven.t.t1.c9

print('~~~~~~~~~~~~~~C15~~~~~~~~~~~~~~~')
print('package:' + (__package__ or '当前模块不属于任何包'))
print('name:' + __name__)
print('doc:' + (__doc__ or '当前模块没有文档注释'))
print('file:' + __file__)

# 如果想让c15以模块被运行，那么就在工程顶级目录运行python -m seven.c15
