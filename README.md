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
   属性查找顺序：。。。

   元类：
