# 练习1:
# 在控制台中输入一个整数
# 如果是奇数 则显示奇数   否则显示偶数
number = int(input("请输入整数:"))
if number % 2 != 0:
    print("是奇数")
else:
    print("是偶数")

# 练习2:
# 在控制台中输入一个年份
# 如果是闰年 则显示闰年   否则显示平年
year = int(input("请输入年份:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("闰年")
else:
    print("平年")