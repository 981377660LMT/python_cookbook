from os.path import join, dirname

file = join(dirname(__file__), '迭代.py')

# 通常来讲， StopIteration 用来指示迭代的结尾。 
# 然而，如果你手动使用 next() 函数的话，
# 你还可以通过返回一个指定值来标记结尾，比如 None
with open(file, 'r', encoding='utf-8') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

