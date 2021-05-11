```py
可迭代对象的解构
a,*b,c=[1,2,3,4,5]
python里不会报错,js里会报错

我们是用逗号生成元组而不是括号
a=1,2
#################################################
如果函数的默认参数是可变的如list dict 则最好使用None作为默认值
def foo(a,b=None):
  if b is None:
    b=[]
################################################
# 测试是否传递默认参数：object()测试同一性
ref=object()

def bar(a,b=ref):
  if b is ref:
    print('b没传')

bar(1)

默认参数的值仅仅在函数定义时赋值一次（特别注意类的__init__)
默认参数必须是不可变对象


# n=n绑定变量,lambda定义时就能绑定到值
funclist = [lambda x, n=n: x + n for n in range(5)]
for func in funclist:
    print(func(0))a

# 切片，字典映射都是getitem的操作

```
