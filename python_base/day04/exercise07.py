"""
    获取最大／最下值
"""

list01 = [34, 5, 6, 78, 9, 0, 5, 8, 88, 4]
# # 假设第一个元素就是最大值
# max = list01[0]
# # 依次与后面（从第二个开始）元素进行比较
# for i in range(1,len(list01)):
# # 发现更大的，则替换假设的．
#     if max  < list01[i]:
#         max = list01[i]
# # 最后假设的就是真的最大值．
# print(max)

# 练习２：查找最小元素
# 假设第一个元素就是最大值
min = list01[0]
# 依次与后面（从第二个开始）元素进行比较
for i in range(1, len(list01)):
    # 发现更大的，则替换假设的．
    if min > list01[i]:
        min = list01[i]
# 最后假设的就是真的最大值．
print(min)


