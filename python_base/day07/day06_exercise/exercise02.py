# 2.参照下列代码，定义根据月份返回天数的方法．
#   要求：考虑２月，如果是闰年返回２９天，否则返回２８天．
#     month = int(input("请输入月份:"))
#     if month < 1 or month > 12:
#         print("输入有误")
#     elif month == 2:
#         print("28天")
#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         print("30天")
#     else:
#         print("31天")

# 向外返回的结果，类型应该统一．
# def get_day_by_month(year,month):
#     if month < 1 or month > 12:
#         return 0
#     elif month == 2:
#         if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
#             return 29
#         else:
#             return 28
#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         return 30
#     else:
#         return 31


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_day_by_month(year, month):
    if month < 1 or month > 12:
        return 0
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


day = get_day_by_month(2019,13)
print(day)
