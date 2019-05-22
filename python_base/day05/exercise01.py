# 练习：使用ｒａｎｇｅ生成１－－１０之间的数字，存入列表list01中．
#      使用列表推导式，将list01中所有奇数存入list02
#                    将list01中所有偶数存入list03
#                    将list01中元素大于３的存储list04

# list01 = []
# for item in range(1,11):
#     list01.append(item)

list01 = [item for item in range(1,11)]
list02 = [item for item in list01 if item % 2 ==1]
list03 = [item for item in list01 if item % 2 ==0]
list04 = [item for item in list01 if item > 3]