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
Semaphore对象：Lock互斥锁的加强版，可以被有限多个线程同时拥有，而Lock只能被某一个线程同时拥有。
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


进程间通信
Queue
# multiprocessing中的queue不能用于pool进程池
# pool中的进程间通信需要使用manager中的queue
通过pipe实现进程间通信
# pipe的性能高于queue
#pipe只能适用于两个进程
共享内存


10. 协程
1999年C10K问题 单核CPU万并发
C10M问题 8核CPU 64G内存 10gbps 1000万并发连接
IO多路复用(select,poll,epoll):一个进程监视多个文件描述符
等待数据+将数据从内核态复制到用户态(还是同步IO)
![](D:/test/python/python基础/py高级/AdvancePython-master/note/2021-07-09-12-08-34.png)

传统函数调用 过程 A->B->C
我们需要一个可以暂停的函数，并且可以在适当的时候恢复该函数的继续执行
出现了协程 -> 有多个入口的函数， 可以暂停的函数， 可以暂停的函数(可以向暂停的地方传入值)


回调模式编码复杂
同步编程并发性不高
**多线程编程需要线程间同步和锁**

协程：采用同步的方式去编写异步代码
使用单线程切换任务:不需要锁，并发性高


yield from
# yield from 后加一个iterable对象=一个一个yield
原理：
"""
看完代码，我们总结一下关键点：

1. 子生成器生产的值，都是直接传给调用方的；调用方通过.send()发送的值都是直接传递给子生成器的；如果发送的是 None，会调用子生成器的__next__()方法，如果不是 None，会调用子生成器的.send()方法；
2. 子生成器退出的时候，最后的return EXPR，会触发一个StopIteration(EXPR)异常；
3. yield from表达式的值，是子生成器终止时，传递给StopIteration异常的第一个参数；
4. 如果调用的时候出现StopIteration异常，委托生成器会恢复运行，同时其他的异常会向上 "冒泡"；
5. 传入委托生成器的异常里，除了GeneratorExit之外，其他的所有异常全部传递给子生成器的.throw()方法；如果调用.throw()的时候出现了StopIteration异常，那么就恢复委托生成器的运行，其他的异常全部向上 "冒泡"；
6. 如果在委托生成器上调用.close()或传入GeneratorExit异常，会调用子生成器的.close()方法，没有的话就不调用。如果在调用.close()的时候抛出了异常，那么就向上 "冒泡"，否则的话委托生成器会抛出GeneratorExit异常。

"""
python 3.5 以前一直用生成器实现协程
python为了将语义变得更加明确，就引入了async和await关键词用于定义原生的协程

await 相当于 yield from

# 协程的调度依然是 事件循环+协程模式 ，协程是单线程模式
不要time.sleep()(阻塞，线程被挂起),而要用await asyncio.sleep(2) （非阻塞）
因为是单线程
对应于js里的Promiseawait new Promise(resolve => {
    setTimeout(() => {
      resolve()
      console.log(666)
    }, 1000)
  } 不是阻塞的(线程不会被挂起)


asyncio.gather类似于Promise.all

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.imooc.com") for i in range(10)]
    loop.run_until_complete(asyncio.gather(*tasks))
    print(time.time() - start_time)


mysqlclient是阻塞的
使用多线程：在携程中集成阻塞io

注意nodejs 爬虫 高并发需要Promise.all实现高并发
```

Python **服务端工程师就业面试指导**(齐）

笔记
优先使用组合而非继承
python 的模块是单例的
微服务+容器架构

Ctrl-C 发送 INT 信号（SIGINT）；默认情况下，这会导致进程终止。

查看端口信息
netstat/lsof netstat -aux |grep 端口
查看内存
free

进程间通信

1. IPC(进程间传递信号或者数据) nodejs 本身提供的 ipc 管道：process.send() 和 process.on('message')
   node 的例子

- 管道(Pipe) 普通流 pipe：child.stdin/stdout
- 信号(Signal 例如 ctrl+c SIGINT)
- 消息队列 redis、消息队列
- 共享内存
- 信号量
- 套接字 socket process.send 可以传递 socket 句柄

操作系统内存管理
分页机制:逻辑地址与内存地址分离
分段机制：数据保护与隔离
虚拟内存：把一部分暂时不用的内存信息放到硬盘上
内存抖动：频繁的页调度

python 垃圾回收(3 个机制)

- 引用计数
  缺点:两个对象相互引用之后引用计数无法归零
- 解决：标记清除(可达的岛屿)+分代回收

幂等:多次请求结果一样(OPTIONS,HEAD,GET,PUT,DELETE)
安全：不修改服务端数据 (OPTIONS,HEAD,GET)

服务端如何区分不同的 http 请求？ Content-Length

IO 多路复用
unix 网络编程五种网络模型
阻塞、非阻塞、IO 多路复用(主要)、信号驱动、异步 IO
提高并发:
老的：多线程/进程
新的：IO 多路复用(select/poll/epoll)

python3 selectors 模块

python 并发网络库
tornado(实现微服务,restful 接口)
gevent (绿色线程，猴子补丁修改内部 socket 非阻塞)
asyncio (原生协程，协程+事件循环)

mysql 基础

- 事务的的并发控制
  四种异常:
  幻读
  非重复读
  脏读
  丢失修改
- 四种事务隔离级别
  读未提交
  读已提交
  可重复读(mysql innodb 默认)
  串行化

乐观锁(版本号时间戳，check and set)&悲观锁(一锁二查三更新,select for update)
怎么选择？

数据库数字类型的 length 并不是大小(大小由类型决定)，是 mysql 数据库中的显示长度

索引工作原理
查找结构进化史
线性查找=>二分查找=>HasH=>二叉查找树(复杂度退化)=>平衡树=>多路查找树=》多路平衡查找树(B-Tree)=>B+树(mysql 索引使用)
B+树特点

1. 只在叶子节点存储数据，非叶子节点存储孩子
2. 叶子节点通过指针相连，实现范围查询

创建索引最佳实践(3 点):

1. 索引字段必须 NOT NULL =>mysql 很难对空值查询优化
2. 作为索引的字段值必须区分度高，不要有大量相同值
3. 索引长度不要太长=》耗时

索引什么时候失效(3 个)：
记忆口诀：模糊匹配，类型隐转，最左匹配
%LIKE
隐式类型转换
最左前缀原则(最左匹配原则就是指在联合索引中，如果你的 SQL 语句中用到了联合索引中的最左边的索引，那么这条 SQL 语句就可以利用这个联合索引去进行匹配)
即 B+树的 key 没有办法比较

聚集索引 非聚集索引
B+ Tree 叶节点存的是指针还是数据
MYISAM 索引与数据分离 存的是非聚集索引
InnoDB 数据文件就是索引文件 主键索引就是聚集索引

排查慢查询(通常是缺少索引)

1. 慢查询日志
2. explain 索引策略

禁止三张表的 join
SQL 语句的连接
内(inner join)、外(left join&right join)、全(full join)

内 指的文氏图的内部(交集)
左右连接 对应文氏图左右
全 并集

缓存的问题(一般是 redis)
作用：解决 mysql 压力；减少响应时间(微秒与毫秒级别差异)；提升吞吐量（单机 QPS 万并发）
数据类型与使用场景(5)
持久化方式(2):快照 dump.rdb/AOF(每一个写命令都记录到文件)
redis 事务()
redis 如何实现分布式锁:键值对设置锁(setnx 实现加锁)
缓存使用模式(3):同时更新/先更新缓存，缓存同步更新数据库/先更新缓存，缓存定期异步更新数据库
缓存的坑
类型|例子|解决方案
-----|-----|-----
缓存穿透|无脑爬虫乱查不存在的数据|没查到返回 NONE，也缓存，设置较短的超时时间
缓存击穿|热点 key 过期|分布式锁:只能由一个线程从数据库拉取数据，然后更新缓存，其他线程等待/异步后台更新:对过期的 key 自动刷新
缓存雪崩|大量缓存同时失效|多级缓存/随机超时/监控报警完善

实事求是 说了解即可

框架考点
WSGI 是什么为什么需要
描述了服务器(uWSGI/Gunicorn)与 python web 应用(django/flask)的接口规范
解决 python web server 乱象(CGI/fastCGI)

MVC:解耦

系统设计
短网址服务/评论服务/feed 流系统/抢红包服务
微服务架构:很多系统被按照业务拆分，需要单独设计一个系统服务
eg:公司提供一个供其他所有业务使用的一个短网址服务(不重新造轮子)

相关领域/算法经验 有架构设计能力
熟悉后端计数组件例如消息队列缓存数据库框架
写文档流程图架构设计图

系统设计三大要素

1. **使用场景**(比如短网址系统给公司用)和**限制条件**(用户量多少,峰值与平均 QPS 估算)
   不要杀鸡牛刀，要对症下药
2. **数据存储**设计(字段、类型、持久化？sql 还是 nosql?索引，优化，缓存)
3. **算法模块**设计(接口设计，什么算法模型，取舍)
   程序=算法+数据结构
   系统=服务+存储
   扩展与容错问题
   设计短网址系统

- eg:如何设计短网址(TinyUrl Service)系统？数据存储系统？
  例如 bitly.com 不超过七位的字符串
  短网址 mysql 即可 字段
  id 原网址 短网址 时间
  给短网址加索引即可
  算法：long_to_short short_to_long
  1. md5 摘要算法取前七个字符；但是冲突

短链接的原理其实就是：

将长链接通过一定的手段生成一个短链接
**访问短链接时实际访问的是短链接服务器，然后根据短链接的参数找回对应的长链接**
**302**重定向跳转(301 永久重定向会无法收集用户来源)

62 表示 26+26+10
**现在业内用得比较多的是发号器（ID 自增)+62 进制编码**

总结：
https://www.zhihu.com/question/20103344
**ID 自增后，转成 62 进制，在 DB 保存映射关系，生成短链接**
当前互联网上的网页总数大概是 45 亿
{62}^7=3521614606208627=3521614606208 个网址，远远大于 45 亿。所以长度为 7 就足够了。
一个长网址，对应多个短网址
以这个 7 位长度的短网址作为唯一 ID，这个 ID 下可以挂各种信息，比如生成该网址的用户名，所在网站，HTTP 头部的 User Agent 等信息，收集了这些信息，才有可能在后面做大数据分析，挖掘数据的价值。短网址服务商的一大盈利来源就是这些数据。
如果一些别有用心的黑客，短时间内向 TinyURL 服务器发送大量的请求，会迅速耗光 ID，怎么办呢？

怎么设计秒杀系统？

1. 消息队列削峰:削峰从本质上来说就是更多地延缓用户请求
2. 负载均衡，分而治之
3. 合理的使用并发和异步

面试准备:算法数据结构+数据库+网络
搜索公司的**面经**
没事多刷算法题
广撒网 多拿几个 offer
从易到难 实事求是
了解对方的技术和业务
手写代码
尽量进入公司核心业务
持续学习，避免增删改查板砖
多了解微服务、serverless、graphql 新技术
