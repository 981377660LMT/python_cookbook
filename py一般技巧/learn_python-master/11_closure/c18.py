origin = 0


def factory(pos):

    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos

    return go


f = factory(origin)
print(f.__closure__[0])
print(f(2))
print(f(3))
print(f(6))
