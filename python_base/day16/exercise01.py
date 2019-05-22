list02 = [2,3,4,6]
# 练习：使用列表推导式，与生成器表达式，获取list02中，大于３的数据．

result01 = [item for item in list02 if item > 3 ] # 本行代码：执行所有操作，保存所有结果
result02 = (item for item in list02 if item > 3 ) # 本行代码：返回生成器对象

for item in result01:# 从结果中获取数据
    print(item)

for item in result02:# 循环一次，计算一次，返回一次
    print(item)
