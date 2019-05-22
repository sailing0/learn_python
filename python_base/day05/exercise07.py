# 练习２：
# ["张三丰", "无忌", "赵敏"]
# [101, 102, 103]
# (1) 根据两个列表形成一个字典：ｋｅｙ姓名，ｖａｌｕｅ房间号
# (2) 将字典的键与值进行翻转．即：ｋｅｙ房间号，ｖａｌｕｅ姓名

list01 = ["张三丰", "无忌", "赵敏"]
list02 = [101, 102, 102]
# dict01 = {}
# for i in range(len(list01)):
#     dict01[list01[i]] = list02[i]

dic02 = {list01[i]: list02[i] for i in range(len(list01))}
print(dic02)

# dic03 = {}
# for key,value in dic02.items():
#     dic03[value] = key

# {101: '张三丰', 102: '赵敏'}   张无忌与赵敏同居，导致ｋｅｙ重复，无忌被覆盖.
dic03 = {value: key for key, value in dic02.items()}
print(dic03)

#[(102, '无忌'), (101, '张三丰'), (102, '赵敏')]
list03 = [(value,key) for key, value in dic02.items()]
print(list03)




