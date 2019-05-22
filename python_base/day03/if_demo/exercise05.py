# 练习1:在控制台中获取一个整数,判断是奇数还是偶数,要求使用真值表达式
number = int(input("请输入整数:"))
# if number % 2 == 1:
if number % 2:  # bool(5 % 2)-->bool(1)  bool(6 % 2)-->bool(0)
    print("奇数")
else:
    print("偶数")

# 练习2:在控制台中获取一个年份,如果是闰年给变量day赋值29,赋值28.
year = int(input("请输入年份:"))
# day = None
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     day = 29
# else:
#     day = 28

# day = 29  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28

day = 29 if not year % 4 and year % 100 or not year % 400 else 28
