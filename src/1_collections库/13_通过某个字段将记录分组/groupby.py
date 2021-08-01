from collections import defaultdict
from pprint import pprint
from itertools import groupby

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows.sort(key=lambda x: x['date'])
# pprint(rows)
a = groupby(rows, key=lambda x: x['date'])
# 在每次迭代的时候，它会返回一个值和一个迭代器对象， 这个迭代器对象可以生成元素值全部等于上面那个值的组中所有对象。
print(dict(a))
# {'07/01/2012': <itertools._grouper object at 0x000001D4C5126FA0>,
# '07/02/2012': <itertools._grouper object at 0x000001D4C5109550>,
# '07/03/2012': <itertools._grouper object at 0x000001D4C5009910>,
# '07/04/2012': <itertools._grouper object at 0x000001D4C5009160>}
for _, item in a:
    for i in item:
        print(i)

# 如果你仅仅只是想根据 date 字段将数据分组到一个大的数据结构中去，
# 并且允许随机访问， 那么你最好使用 defaultdict() 来构建一个多值字典
row_by_date = defaultdict(list)
for row in rows:
    row_by_date[row['date']].append(row)

print(row_by_date['07/04/2012'])
