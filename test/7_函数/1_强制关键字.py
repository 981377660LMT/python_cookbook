# import html

# print(html.escape('""& <>'))

# 将参数放在*args后面即可
def foo(maxsize, *args, block):
    pass


# foo() missing 1 required keyword-only argument: 'block'
# foo(1024,1)
foo(1024, block=False)
##############################################


def minimum_with_clap(*values, clip=None):
    min_value = min(values)
    if clip is not None:
        min_value = clip if clip > min_value else min_value
    return min_value


print(minimum_with_clap(1, 2, 3, 4, clip=2))
