# 3.参照下列代码，定义获取最小值方法．
#     min = list01[0]
#     for i in range(1, len(list01)):
#         # 发现更大的，则替换假设的．
#         if min > list01[i]:
#             min = list01[i]
#     print(min)

def get_min(list_target):
    min = list_target[0]
    for i in range(1, len(list_target)):
        if min > list_target[i]:
            min = list_target[i]
    return min


min = get_min([2, 3, 45, 1, 9, 3])
print(min)
