# AdvancePython

2. python 一切皆对象

   对象的三个特征：身份、内存和值

身份：在内存中的地址，可以用 id(变量)函数来查看
类型：任何变量都必须有类型
值
两个值为 None 的变量地址完全相同，可见 None 是全局唯一的

1. 魔法方法 协议

2. 类与对象
   抽象基类应用场景:去检查某个类是否有某种方法;需要强制某个子类必须实现某些方法
   isinstance 和 type 区别:isinstance 回去继承链上查找,type 不会
   isinstance 的工作原理是
   查找属性使用 MRO 算法(c3 算法)
   用 staticmethod 完成初始化不太好;适合提供一些 utils 函数
   用 classmethod 完成初始化,不需要硬编码
   获取私有属性\_A\_\_attr
   自省机制:自省是通过一定的机制查询到对象的内部结构
   通过**dict**查询属性与值/通过 dir 获取所有的属性名
   调用 super 的逻辑初始化:super 不是调用父类的构造函数,而是调用**mro**链下一个类的构造函数
   mixin 模式特点

   1. Mixin 类功能单一
   2. 不和基类关联，可以和任意基类组合， 基类可以不和 mixin 关联就能初始化成功
   3. 在 mixin 中不要使用 super 这种用法
      import contextlib

   上下文管理器：contextmanager 可以简化上下文管理器，不需要我们编写**enter**和**exit**函数

   ```py
   @contextlib.contextmanager
   def file_open(file_name):
       print ("file open")
       yield {}
       print ("file end")

   with file_open("bobby.txt") as f_opened:
       print ("file processing")
   ```

3. 序列类
   extend 方法和 append 方法区别
   extend(iterable) 相当于 js 的 push(...iterable)，append(a) 相当于 js 的 push(a)
   可切片是**getitem**方法实现的
   self 是对象，type(self)表示这个对象的 class,item 是切片 slice 对象或者 int 对象

   ```py
       def __getitem__(self, item):
        cls = type(self)
        print(self, item)
        if isinstance(item, slice):
            return cls(staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(
                staffs=[self.staffs[item]],
            )

   ```

   需要维持一个排序的序列时，使用 bisect 操作
   什么时候不应该使用 list：array 性能比 list 高

4. 深入 dict 和 set
   dict 的 abc 继承关系：dict 属于 mapping 类型
   避免获取不存在的字典键 KeyError：使用 my_dict.get(key,default) 方法
   setdefault 方法：

   ```py
   Insert key with a value of default if key is not in the dictionary.

   Return the value for key if key is in the dictionary, else default.
   ```

   update 方法：相当于 Object.assign 方法

   dict 的子类：collections.defaultdict 重写了**missing**方法，不会有 KeyError

   ```py
       def __missing__(self, key):
        print(key)
        return 1
   ```

   set 和 frozenset：

   ```py
       b = {{1}: 2}
      TypeError: unhashable type: 'set'
      这是因为字典的键不能变
      那么哪些是可哈希元素？哪些是不可哈希元素？
      可哈希的元素有：int、float、str、tuple
      不可哈希的元素有：list、set、dict
      应使用
      b = {frozenset({1}): 2}使键变为immutable
   ```

   dict 的性能远远大于 list
   在 list 中随着 list 数据的增大 查找时间会增大
   在 dict 中查找元素不会随着 dict 的增大而增大

   dict 与 set 实现原理
   hash 表
   dict 的 key 或者 set 的值 都必须是可以 hash 的
   不可变对象 都是可 hash 的， str， fronzenset， tuple，自己实现的类 **hash**
   dict 的内存花销大，但是查询速度快， 自定义的对象 或者 python 内部的对象都是用 dict 包装的

5. python 对象引用和垃圾回收
   垃圾回收机制：两种,对象是否可以被回收的两种经典算法: 引用计数法 和 可达性分析算法

   - python 中，万物皆对象。python 中不存在所谓的传值调用，一切传递的都是对象的引用，也可以认为是传址。
     a=不可变类型
     b=不可变类型
     则 a is b
     a=可变类型
     b=可变类型
     则 as is not b

   ```py
   a = 1
   b = 1
   True
   print(a is b)
   a=[]
   b=[]
   False
   print(a is b)
   ```

   ```py
   person = People()
   if type(person) is People:
    print("yes")
   ```

   不要给构造函数默认参数设置可变类型 def **init**(self, staffs=[]):
   实例会共用这个默认参数
   当函数被定义时，Python 的默认参数就被创建一次，而不是每次调用函数的时候创建。
   应该写

   ```py
   def append_to(self, staffs=None):
    if staffs is None:
        staffs = []
   ```

6. 元编程
   @property 计算属性的 getter
   @foo.setter 计算属性的 setter

   两个魔法方法：
   **getattr** 就是在查找不到属性的时候调用
   **getattribute**是在访问所有属性时的时候((包括不存在的 key))(劫持属性)

   ```py
   如果user是某个类的实例，那么user.age（以及等价的getattr(user,’age’)）
   首先调用__getattribute__。如果类定义了__getattr__方法，
   那么在__getattribute__抛出 AttributeError 的时候就会调用到__getattr__
   ```

   三个属性描述符(PropertyDescriptor)：**get**,**set**,**delete**
   一个类只要实现任一个方法，那这个类就是属性描述符

   属性查找顺序:
   如果 user 是某个类的实例，那么 user.age（以及等价的 getattr(user,’age’)）
   首先调用**getattribute**。如果类定义了**getattr**方法，
   那么在**getattribute**抛出 AttributeError 的时候就会调用到**getattr**，
   而对于描述符(**get**）的调用，则是发生在**getattribute**内部的。
   user = User(), 那么 user.age 顺序如下：

<!-- 1.先找数据描述符：这是个好特性 -->

（1）如果“age”是出现在 User 或其基类的**dict**中， 且 age 是 data descriptor， 那么调用其**get**方法, 否则

<!-- 2.再找实例的__dict__ -->

（2）如果“age”出现在 user 的**dict**中， 那么直接返回 obj.**dict**[‘age’]， 否则

<!-- 3.再找类的__dict__ -->

（3）如果“age”出现在 User 或其基类的**dict**中

（3.1）如果 age 是 non-data descriptor，那么调用其**get**方法， 否则

（3.2）返回 **dict**[‘age’]

<!--4. 找不到则getattr -->

（4）如果 User 有**getattr**方法，调用**getattr**方法，否则

<!--5. 抛出错误 -->

（5）抛出 AttributeError

new 和 init:用于框架重写

```py
class User:
    def __new__(cls, *args, **kwargs):
        print(" in new ")
        return super().__new__(cls)

    def __init__(self, name):
        print(" in init")
        pass


a = int()
# new 是用来控制对象的生成过程， 在对象生成之前
# init是用来完善对象的
# 如果new方法不返回对象， 则不会调用init函数
if __name__ == "__main__":
    user = User(name="bobby")




元类：
# 元类是创建类的东西
def say(self):
    return "i am user"
    # return self.name

Base = type("User", (object,), {'name': 'cmnx', 'say': say})
User = type("User", (Base,), {})

另一种写法：metaclass=''
所有metaclass都必须继承type类
class MetaClassShouldExtendsType(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
元类可以控制类生成的过程
# python中类的生成过程，会首先向上寻找metaclass，通过metaclass去创建类
# 找不到则用type创建类,调用type.__new__()
class MetaUser(metaclass=MetaClassShouldExtendsType):
    pass
用法;metaclass=ABCMeta
ABCMeta重写了__new__函数，在返回实例self前进行属性检查，是否实现了抽象方法等

orm实现



7.iterable与iterator
iterable里面有__iter__
iterator里卖弄有__next__
迭代器和以下标的访问方式不一样， 迭代器是不能返回的, 迭代器提供了一种惰性方式数据的方式

生成器读取大文件
in 定位到对的__iter__ 找不到则__getitem__
from collections.abc import Iterator

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)

    # def __getitem__(self, item):
    #     return self.employee[item]


class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        #真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

生成器generator 里卖弄有__next__
# 生成器函数，函数里只要有yield关键字
# 生成器推导式(i for i in range(10))
# 生成器对象， python编译字节码的时候就产生了，

def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1


for data in gen_fib(10):
    print(data)
# print (gen_fib(10))
# 斐波拉契 0 1 1 2 3 5 8
# 惰性求值， 延迟求值提供了可能

生成器原理：Heap Memory
# python一切皆对象，栈帧对象， 字节码对象
# 当foo调用子函数 bar， 又会创建一个栈帧
# 所有的栈帧都是分配在堆内存上，这就决定了栈帧可以独立于调用者存在
# 任何地方都可以调用生成器对象
# 上次的调用结果保存在堆里
# g.gi_frame.f_lasti保存上一次的位置
# g.gi_frame.f_locals保存生成器局部变量

def gen_func():
    yield 1
    name = "bobby"
    yield 2
    age = 30
    return "imooc"


g = gen_func()

print(g.__next__(), g.gi_frame.f_lasti, g.gi_frame.f_locals)
print(g.__next__(), g.gi_frame.f_lasti, g.gi_frame.f_locals)
print(g.__next__(), g.gi_frame.f_lasti, g.gi_frame.f_locals)
# 1 2 {}
# 2 12 {'name': 'bobby'}
# Traceback (most recent call last):
#   File "e:\test\python\python基础\py高级\AdvancePython-master\9_迭代器生成器.py\6_gen_test.py", line 13, in <module>
#     print(g.__next__(), g.gi_frame.f_lasti, g.gi_frame.f_locals)
# StopIteration: imooc

JS的生成器函数
function* gen() {
  const a = yield 1
  // return为迭代器的最后一次迭代（当done等于时true）提供返回值。
  return a * 2
}

const g = gen()

// console.log(g.next())
// console.log(g.next(3))

// # 如果使用for ... of循环或类似方法通过迭代器进行迭代Array.from，则该return值将被忽略
for (const item of g) {
  console.log(item)
}

生成器应用：读取500G大文件：只有一行，内存放不下
# 500G, 特殊 一行
def myreadlines(f, newline):
    """读取大文件

    Args:
        f (TextIOWrapper): 文件句柄
        newline (str): 分隔符

    Yields:
        list: buff字段
    """
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline) :]
        chunk = f.read(30)

        if not chunk:
            # 说明已经读到了文件结尾
            yield buf
            break
        buf += chunk


# f.read()里可以传size限制
with open("input.txt") as f:
    for line in myreadlines(f, "{|}"):
        print(line)

8.socket编程
操作系统为我们提供了操作传输层协议的api socket

9.多进程多线程编程
# gil会根据执行的字节码行数以及时间片释放gil，gil在遇到io的操作时候主动释放

线程通信方法:共享全局变量；Queue，线程安全
线程变量同步方法:Lock/RLokc;Condition;Semaphore;Event
Lock & RLock：互斥锁，用来保证多线程访问共享变量的问题
Semaphore对象：Lock互斥锁的加强版，可以被多个线程同时拥有，而Lock只能被某一个线程同时拥有。
Event对象：它是线程间通信的方式，相当于信号，一个线程可以给另外一个线程发送信号后让其执行操作。
Condition对象：其可以在某些事件触发或者达到特定的条件后才处理数据
原文链接：https://blog.csdn.net/brucewong0516/article/details/81050939
# 调用acquire([timeout])时，线程将一直阻塞，
# 直到获得锁定或者直到timeout秒后（timeout参数可选）。
# 返回是否获得锁。
# 1. 用锁必然会影响性能
# 2. 锁会引起死锁(同一个线程或者不同线程竞争同一把锁)
RLock可重入的锁
# 在同一个线程里面，可以连续调用多次acquire， 一定要注意acquire的次数要和release的次数相等，否则死锁
Condition条件变量：对接古诗
# 条件变量， 用于复杂的线程间同步
发布与订阅：
Condition.notify()
Condition.wait()

Condition.acquire()  (enter时调用acquire方法，即RLock的acquire)
Condition.release()  (exit时调用release方法，即RLock的release)
 # 启动顺序很重要
    # 在调用with cond之后才能调用wait或者notify方法
    # condition有两层锁， 一把底层锁会在线程调用了wait方法的时候释放， 上面的锁会在每次调用wait的时候分配一把并放入到cond的等待队列中，等到notify方法的唤醒
Condition对象维护了一个锁（Lock/RLock)和一个waiting池。
class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        # acquire获得Condition对象的锁
        # Condition对象的构造函数可以接受一个Lock/RLock对象作为参数，如果没有指定，则Condition对象会在内部自行创建一个RLock
        with self.cond:
            # 调用wait方法时，线程会释放Condition内部的锁并进入blocked状态，同时在waiting池中记录这个线程
            self.cond.wait()
            print("{} : 在 ".format(self.name))
            # 当调用notify方法时，Condition对象会从waiting池中挑选一个线程，通知其调用acquire方法尝试取到锁
            # 处于waiting池的线程只能通过notify方法唤醒
            self.cond.notify()


Semaphore信号量
# Semaphore 是用于控制进入数量的锁
# 文件， 读、写， 写一般只是用于一个线程写，读可以允许有多个
# 限制爬虫数量
```
