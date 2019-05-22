"""
    累加1 -- 100 之间 能被3 整除的整数和

"""
# sum = 0
# for item in range(1,100):
#     # 如果满足条件 则 累加
#     if item % 3 == 0:
#         sum += item
# print(sum)


sum = 0
for item in range(1,100):
    # 如果不满足条件 则 跳过
    if item % 3 != 0:
        continue# 跳过
    sum += item
print(sum)










