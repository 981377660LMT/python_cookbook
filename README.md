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

# 切片，字典，映射[]取值都是__getitem__的操作

# 传统的编程语言，早有异步编程的解决方案（其实是多任务的解决方案）。其中有一种叫做"协程"（coroutine），意思是多个线程互相协作，完成异步任务。
# 第一步，协程A开始执行。
# 第二步，协程A执行到一半，进入暂停，执行权转移到协程B。
# 第三步，（一段时间后）协程B交还执行权。
# 第四步，协程A恢复执行。
# 读取文件的协程写法如下。
function asnycJob() {
  // ...其他代码
  var f = yield readFile(fileA);
  // ...其他代码
}
# asyncJob 是一个协程，它的奥妙就在其中的 yield 命令。它表示执行到此处，执行权将交给其他协程。也就是说，yield命令是异步两个阶段的分界线。
# 协程遇到 yield 命令就暂停，等到执行权返回，再从暂停的地方继续往后执行。它的最大优点，就是代码的写法非常像同步操作
# Generator 函数是协程在 ES6 的实现，最大特点就是可以交出函数的执行权（即暂停执行）。

# 传入回调函数信息：对象/闭包/协程/partial
至少有两种主要方式来捕获和保存状态信息，你可以在一个对象实例(通过一个绑定方法)或者在一个闭包中保存它。 两种方式相比，闭包或许是更加轻量级和自然一点，因为它们可以很简单的通过函数来构造。 它们还能自动捕获所有被使用到的变量。因此，你无需去担心如何去存储额外的状态信息(代码中自动判定)。
```
