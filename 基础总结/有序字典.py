# -*- coding: utf-8 -*-
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2

od.move_to_end('a')
od.popitem(last=False)
# od.popitem(last=True)

print(od)
print('a' in od)
