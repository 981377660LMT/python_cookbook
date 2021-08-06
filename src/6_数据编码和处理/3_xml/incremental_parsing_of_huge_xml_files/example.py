# Example of incremental XML parsing
#
# The file 'potholes.xml' is a greatly condensed version of a larger
# file available for download at
#
# https://data.cityofchicago.org/api/views/7as2-ds3y/rows.xml?accessType=DOWNLOAD
# 你想使用尽可能少的内存从一个超大的XML文档中提取数据。
# 任何时候只要你遇到增量式的数据处理时，第一时间就应该想到迭代器和生成器

from xml.etree.ElementTree import iterparse


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


# Find zip code with most potholes

from collections import Counter

potholes_by_zip = Counter()

data = parse_and_remove('potholes.xml', 'row/row')
for pothole in data:
    potholes_by_zip[pothole.findtext('zip')] += 1

for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)
