from contextlib import suppress

# 遇到TypeError不报错而是直接退出
with suppress(TypeError):
    print(666)
    1 + "1"
    1 / 0

print(1)
