# example.py
#
# Various samples of reading CSV files

import csv

# (a) Reading as tuples

print('Reading as tuples:')
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # process row
        # row 会是一个列表。因此，为了访问某个字段，你需要使用下标
        print('    ', row)

# (b) Reading as namedtuples

print('Reading as namedtuples')
from collections import namedtuple

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    Row = namedtuple('Row', next(f_csv))
    for r in f_csv:
        row = Row(*r)
        # Process row
        # 它允许你使用列名如 row.Symbol 和 row.Change 代替下标访问
        print('    ', row)


# (c) Reading as dictionaries

print('Reading as dicts')
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # process row
        # 在这个版本中，你可以使用列名去访问每一行的数据了。比如，row['Symbol'] 或者 row['Change']
        print('    ', row)

# (d) Reading into tuples with type conversion

print('Reading into named tuples with type conversion')

col_types = [str, float, str, str, float, int]
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversions to the row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        print(row)

# (e) Converting selected dict fields

print('Reading as dicts with type conversion')

field_types = [('Price', float), ('Change', float), ('Volume', int)]

with open('stocks.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key])) for key, conversion in field_types)
        print(row)

