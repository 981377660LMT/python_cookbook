origin = 0


def go(step):
    global origin
    origin = origin + step
    return origin


print(go(2))
print(go(3))
print(go(6))
