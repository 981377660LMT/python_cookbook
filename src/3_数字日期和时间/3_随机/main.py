import random
random.seed(666)

v = [1, 2, 3, 4]
print(random.choice(v))
print(random.sample(v, 2))

random.shuffle(v)
print(v)
# random 模块使用 Mersenne Twister 算法来计算生成随机数