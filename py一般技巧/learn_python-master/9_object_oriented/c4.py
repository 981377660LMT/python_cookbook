# 面向对象
# 有意义的面向对象的代码
# 类 = 面向对象
# 类、对象
# 类最基本的作用：封装
# 类和对象


# 模板
class Student():
    sum = 0
    # 数据成员，但是下面两个是类变量，但是下面两个变量作为类变量是不太合适的
    name = 'qiyue'
    age = 0

    # 类变量 实例变量
    # 实例方法
    def __init__(self, name, age, score=0):
        # 构造函数
        # 初始化对象的属性，下面两个才是示例变量
        self.name = name
        self.age = age
        self.__score = score
        print(Student.name)
        print(Student.age)
        # Student.sum += 1
        # print('student')
        # 构造函数只能返回None
        print('当前班级学生总数为:', self.__class__.sum)

    # 最前面有双下划线就是私有
    def marking(self, score):
        if score < 0:
            return '不能给别人打负分'
        self.__score = score
        print(self.name, '同学本次考试分数为:', score)

    # 行为 与 特征
    # 方法
    # 实例方法
    def do_homework(self):
        print('homework')

    # 类方法
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

    # 静态方法不需要传入self或cls
    @staticmethod
    def add(x, y):
        print(Student.sum)
        # print(self.name)
        pass

    # 类只负责定义，不负责运行
    # print_file()


class StudentHomework():
    homework_name = ''


class Printer():

    def print_file(self):
        print('name:', self.name)
        print('age:', self.age)


# 方法 和 函数的区别
# 方法：设计层面
# 函数：程序运行、过程式的一种称谓
# student = Student()
# student.print_file()

student1 = Student('石敢当', 18)
# a = student1.__init__()
# print(a)
# print(type(a))
student2 = Student('喜小乐', 19)
# student3 = Student()
# print(id(student1))
# print(id(student2))
# print(id(student3))

print(student1.name)
# print(Student.plus_sum())
student1.plus_sum()
print(student2.name)
print(Student.plus_sum())
print(Student.name)
print(Student.plus_sum())

print(student1.__dict__)
print(Student.__dict__)
print(Student.sum)

student1.add(1, 2)
Student.add(1, 2)
student1.marking(59)
# 这里的__score和成员变量__score是不同的
student1.__score = -1
print(student1.__score)
# 打印出来的_Student__score是成员变量，__score是赋值的变量
print(student1.__dict__)
print(student1._Student__score)
