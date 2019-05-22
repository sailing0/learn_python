# 练习2:在控制台中输入一个季度
# 显示该季度中的月份
season = int(input("请输入季度:"))
if season < 1 or season > 4:
    print("输入有误")
elif season == 1:
    print("有1,2,3月")
elif season == 2:
    print("有4,5,6月")
elif season == 3:
    print("有7,8,9月")
else:
    print("有10,11,12月")









