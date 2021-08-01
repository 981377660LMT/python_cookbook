from datetime import datetime

text = '2012-09-20'

print(datetime.strptime(text, '%Y-%m-%d'))

# 还有一点需要注意的是， strptime() 的性能要比你想象中的差很多， 因为它是使用纯Python实现，并且必须处理所有的系统本地设置。
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))


print(parse_ymd('2020-01-3'))
