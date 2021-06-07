# 500G, 特殊 一行
def myreadlines(f, newline):
    """读取大文件

    Args:
        f (TextIOWrapper): 文件句柄
        newline (str): 分隔符

    Yields:
        list: buff字段
    """
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline) :]
        chunk = f.read(30)

        if not chunk:
            # 说明已经读到了文件结尾
            yield buf
            break
        buf += chunk


# f.read()里可以传size限制
with open("input.txt") as f:
    for line in myreadlines(f, "{|}"):
        print(line)
