#     一注彩票７个球
# 　　前六个是红球：１　－－　３３　之间的数字，且不能重复．
#     最后一个是蓝球：１　－－　１６　之间的数字
#     （１）　在控制台中购买彩票

ticket = []
# 前六个红球：
while len(ticket) < 6:
    number = int(input("请输入第%d个红球号码："%(len(ticket) + 1)))
    if number <1 or number > 33:
        print("不再范围内")
    elif number in ticket:
        print("该号码已经存在")
    else:
        ticket.append(number)
# 蓝球：
while True:
    number = int(input("请输入蓝球号码："))
    if 1<= number <= 16:
        ticket.append(number)
        break # 退出循环
    else:
        print("不再范围内")


print(ticket)  # 只是将列表转换为字符串　再显示

# 获取每个元素
# for item in ticket:
#     print(item)







