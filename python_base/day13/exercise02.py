import time


# 练习1:定义函数, 输入年月日,返回星期.
#  星期一  星期二  星期三  ......
def get_week(year, month, day):
    time_tuple = time.strptime("%d/%d/%d" % (year, month, day), "%Y/%m/%d")
    weeks = {
        0: "星期一",
        1: "星期二",
        2: "星期三",
        3: "星期四",
        4: "星期五",
        5: "星期六",
        6: "星期日",
    }
    # time_tuple[6] 从时间元组中获取星期数
    return weeks[time_tuple[6]]


print(get_week(2019, 4, 18))


# 练习2:定义函数:根据生日(年月日),返回活了多少天.
# -- 根据年月日构建时间元组
# -- 根据构建的时间元组获取时间戳
# -- 使用当前时间戳 - 生日的时间戳
# -- 将活的秒数换算为天
def life_days(year, month, day):
    time_tuple = time.strptime("%d/%d/%d" % (year, month, day), "%Y/%m/%d")
    # time.mktime( time_tuple)
    life_seconds = time.time() - time.mktime(time_tuple)
    return life_seconds / 60 / 60 // 24


print(life_days(1984, 6, 11))
