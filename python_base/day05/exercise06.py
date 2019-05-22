# 练习１：["张三丰","无忌","赵敏"] --> {"张三丰":3,"无忌":2,"赵敏",2}
list01 = ["张三丰", "无忌", "赵敏"]
dict01 = {}
for item in list01:
    dict01[item] = len(item)

dic02 = { item:len(item)  for item in list01}
print(dic02)











