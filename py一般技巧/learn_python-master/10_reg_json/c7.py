import re

s = 'abc, acc, adc, aec, afc, ahc'

# a[cfd]c   匹配  acc, afc, adc
# a[^cfd]c  匹配  abc, aec, ahc
# a[c-f]c   匹配  acc, adc, aec, afc
r = re.findall('a[c-f]c', s)
print(r)
