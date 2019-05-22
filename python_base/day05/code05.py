"""
    字典推导式

"""

# ｋｅｙ：数字　　　ｖａｌｕｅ：数字平方
# dic01 = {}
# for item in range(1,10):
#     dic01[item] = item ** 2
#
# print(dic01)
#
# dic01 = {item:item ** 2 for item in range(1,10)}

dic01 = {}
for item in range(1, 10):
    if item % 2 == 0:
        dic01[item] = item ** 2

dic01 = {item: item ** 2 for item in range(1, 10) if item % 2 == 0}
print(dic01)











