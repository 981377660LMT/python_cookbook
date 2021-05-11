# example.py
#
# Sort a list of a dicts on a common key
# 通过某个关键字排序一个字典列表
from pprint import pprint
from operator import itemgetter
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))


print("Sorted by fname:")
pprint(rows_by_fname)

print("Sorted by uid:")
pprint(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print("Sorted by lname,fname:")
pprint(rows_by_lfname)
