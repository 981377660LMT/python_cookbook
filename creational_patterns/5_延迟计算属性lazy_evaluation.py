# 使用延迟计算属性：将一个类的属性/方法保存为这个类的描述器(存在于类上)
# 当实例访问类上的属性时才在__dict__里生成对应的值
class lazy_property:
    def __init__(self, function) -> None:
        self.function = function

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            # 只在访问的时候才会计算结果
            # 一旦被访问后，结果值将被存入实例的__dict__
            # 因为lazy_property是非数据描述符，所以再次访问时会先访问实例__dict__里的属性而不是类上的属性描述符了
            value = self.function(instance)
            setattr(instance, self.function.__name__, value)
            return value


class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count2 = 0

    @lazy_property
    def relatives(self):
        # Get all relatives, let's assume that it costs much time.
        print(666)
        relatives = "Many relatives."
        return relatives


if __name__ == '__main__':
    Jhon = Person('Jhon', 'Coder')
    print(Jhon.__dict__)
    print(Jhon.relatives)
    print(Jhon.relatives)
    print(Jhon.relatives)
    print(Jhon.__dict__)
