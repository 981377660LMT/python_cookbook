# 面向对象
# 有意义的面向对象的代码
# 类 = 面向对象
# 类、对象
# 类最基本的作用：封装
# 类和对象


# 模板
class Student():
    # 数据成员，但是下面两个是类变量，但是下面两个变量作为类变量是不太合适的
    name = 'qiyue'
    age = 0

    # 类变量 实例变量
    def __init__(self, name, age):
        # 构造函数
        # 初始化对象的属性，下面两个才是示例变量
        self.name = name
        self.age = age
        # print('student')
        # 构造函数只能返回None

    # 行为 与 特征
    # 方法
    def do_homework(self):
        print('homework')

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
print(student2.name)
print(Student.name)

print(student1.__dict__)
print(Student.__dict__)
