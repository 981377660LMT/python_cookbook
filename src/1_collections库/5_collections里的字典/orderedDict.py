# js里的map相当于orderedDict
from collections import OrderedDict
from json import dumps

# 你想精确控制以 JSON 编码后字段的顺序，你可以先使用 OrderedDict 来构建这样的数据
# OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。每次当一个新的元素插入进来的时候， 它会被放到链表的尾部。
# 需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。
od = OrderedDict()
od['a'] = 2
od['3'] = 2
print(dumps(od))
