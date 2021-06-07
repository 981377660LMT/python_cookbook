# 旅行者
x = 0
# 3 result = 3
# 5 result = 8
# 6 result = 14


def step(save):
    save = save

    def do_step(x):
        return save + x

    return do_step


f = step(0)
save = f(3)
print(save)
f = step(save)
save = f(5)
print(save)
f = step(save)
save = f(6)
print(save)
