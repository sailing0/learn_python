# 闰年判断:
# 条件1:  年份能被4整除,但是不能被100整除.
# 条件2:  年份能被400整除
# 在控制台中获取年份
# 判断是否为闰年,如果是显示true,否则显示false

year = int(input("请输入年份:"))
result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(result)













