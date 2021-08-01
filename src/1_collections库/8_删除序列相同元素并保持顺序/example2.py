# example2.py
#
# Remove duplicate entries from a sequence while keeping order


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    a = [{'x': 2, 'y': 3}, {'x': 1, 'y': 4}, {'x': 2, 'y': 3}, {'x': 2, 'y': 3}, {'x': 10, 'y': 15}]
    print(a)
    print(list(dedupe(a, key=lambda a: (a['x'], a['y']))))

# 果如果你想读取一个文件，消除重复行，你可以很容易像这样做：
# with open(somefile,'r') as f:
# for line in dedupe(f):
#     ...