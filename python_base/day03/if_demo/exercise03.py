# 练习3:在控制台中输入一个月份,11:30
# 返回该月份的天数
# 1  3   5   7  8   10   12   --->   31 天
# 4  6   9   11 --->  30 天
# 2  ---> 28 天
month = int(input("请输入月份:"))
if month < 1 or month > 12:
    print("输入有误")
elif month == 2:
    print("28天")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30天")
else:
    print("31天")



