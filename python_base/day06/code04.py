"""
    列表推导式嵌套
"""
list01 = ["a", "b", "c"]
list02 = ["A", "B", "C"]
# list03 = []
# for r in list01:
#     for c in list02:
#         list03.append(r+c)

list03 = [r + c for r in list01 for c in list02]
print(list03)

# 练习：实现两个列表的全排列
#["香蕉","苹果","哈密瓜"]    ["可乐","牛奶"]
list03 = ["香蕉","苹果","哈密瓜"]
list04 = ["可乐","牛奶"]
list05 = []
for r in list03:
    for c in list04:
        list05.append(r+c)

list06 = [r+c for r in list03 for c in list04]
print(list06)





