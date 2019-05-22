"""
    字典
    练习：ｅｘｅｒｃｉｓｅ０４／０５
"""

# 创建空字典
d01 = {}
d02 = dict()

d01 = {"a":"A","b":"B"}
# d01 = dict("ab") # 分不清key  value
d01 = dict([(1,2),(3,4)]) # {1: 2, 3: 4}


#　第一次增加
d01["c"] = "C"
#　第二次修改
d01["c"] = "CC"

# 读取元素(如果不存在则异常)
# 建议：在字典中读取元素，先判断存在，在进行读取．
if "d" in d01:
    print(d01["d"])

print(d01)
# 删除
del d01["c"]
print(d01)

# 获取字典中所有元素：
for key in d01:
    print(key)
    print(d01[key])

# 获取字典中所有记录(元组)
for item in d01.items():
    print(item[0]) # ｋｅｙ
    print(item[1]) # value

for k,v in d01.items():
    print(k) # ｋｅｙ
    print(v) # value

# 获取所有键
for k in d01.keys():
    print(k)

# 获取所有值
for v in d01.values():
    print(v)









