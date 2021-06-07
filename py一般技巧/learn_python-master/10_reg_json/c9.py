# 边界匹配
import re
qq = '123456789'

# 4-8位，前面加^后面加$
r = re.findall('^\d{4,8}$', qq)
print(r)
