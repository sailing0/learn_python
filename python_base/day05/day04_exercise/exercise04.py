#     一注彩票７个球
# 　　前六个是红球：１　－－　３３　之间的数字，且不能重复．
#     最后一个是蓝球：１　－－　１６　之间的数字
#     （２）　随机产生一注彩票

import random


ticket = []
while len(ticket) < 6:
    number = random.randint(1,33)
    if number not in ticket:
        ticket.append(number)

# 排序
# ticket.sort()

# number = random.randint(1,16)
# ticket.append(number)
ticket.append(random.randint(1,16))

# 需求：对列表执行范围的元素进行排序
# (1)通过切片返回新列表
temp = ticket[:6]
# (2)对新列表进行排序
temp.sort()
# (3)将新列表赋值给原列表
ticket[:6] = temp

print(ticket)






