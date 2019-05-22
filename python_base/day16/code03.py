"""
    生成器表达式
    练习：exercise01 exercise02
"""

list01 = [2,3,4,6]
# result = []
# for item in list01:
#     result.append(item ** 2)

# 列表推导式[]     字典推导式 {键:值　for ...}   集合 { for ... }
result = [item ** 2 for item in list01]
print(result)

# def fun01(target):
#     for item in target:
#         yield item ** 2
# 生成表达式
# for item in fun01(list01):
#     print(item)

result = (item ** 2 for item in list01)
for item in result:
    print(item)

