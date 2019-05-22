# 定义根据月份，判断季节的方法．
def get_season(month):
    if month < 1 or month > 12:
        return "输入有误"
    if month <= 3:
        return "春天"
    if month <= 6:
        return "夏天"
    if month <= 9:
        return "秋天"
    return "冬天"


print(get_season(5))
print(get_season(15))
