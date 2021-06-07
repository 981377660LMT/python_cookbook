# 可变关键字参数
def city_temp(**param):
    print(param)
    print(type(param))
    for key, value in param.items():
        print(key, ':', value)
    pass


city_temp(bj='32c', xm='23c', sh='31c')

a = {'bj': '32c', 'sh': '31c'}
city_temp(**a)

# 什么都不传
city_temp()


# 必须参数+可变关键字参数
def city_temp1(param1, **param):
    print(param1)
    print(param)
    print(type(param))
    for key, value in param.items():
        print(key, ':', value)
    pass


city_temp1(1)
