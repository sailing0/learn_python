# 计算最大数
# 思路:假设第一个变量就是最大值,
#     然后一次与下面的几个变量进行比较,如果还有更大的则替换假设的.
num01 = 8
num02 = 6
num03 = 10
num04 = 5


max_value = num01
if max_value < num02:
    max_value = num02
if max_value < num03:
    max_value = num03
if max_value < num04:
    max_value = num04
print(max_value)

