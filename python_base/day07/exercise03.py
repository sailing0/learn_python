# 练习：定义函数，根据天／小时／分钟，计算总秒数

def get_total_second(day=0, hour=0, minute=0):
    return day * 24 * 60 * 60 + hour * 60 * 60 + minute * 60


s01 = get_total_second(1, 1, 1)
s02 = get_total_second(1, 1)
s02 = get_total_second(hour=2)
# 17:00
