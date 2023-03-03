# 写一个方法，验证两个时间戳间隔的天数
# 2018-1-1 2018-1-3 间隔2天
# 2018-1-1 2018-1-1 间隔0天
# 2018-1-1 2018-1-2 间隔1天

import datetime

def get_days(start, end):
    start = datetime.datetime.strptime(start, '%Y-%m-%d')
    end = datetime.datetime.strptime(end, '%Y-%m-%d')
    return (end - start).days

print(get_days('2018-1-1', '2018-1-3'))
print(get_days('2018-1-1', '2018-1-1'))
print(get_days('2018-1-1', '2018-1-2'))

