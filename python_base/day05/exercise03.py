# 练习２：在控制台中输入月，日．
#        计算这是一年的第几天．
# 例如：３月５日
#      累加１月，２月总天数，再累加３月的５天．
# 例如：５月１０日
#      累加１月，２月，３月，４月总天数，再累加５月的１０天．


# month = int(input("请输入月份："))
# day = int(input("请输入天："))
# day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# result = 0
# # 累加前几个月
# for i in range(month - 1):
#     result += day_of_month[i]
# # 累加当月
# result += day
# print(result)


month = int(input("请输入月份："))
day = int(input("请输入天："))
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# 累加前几个月
result = sum(day_of_month[:month - 1])
# 累加当月
result += day
print(result)

#15:33 上课






