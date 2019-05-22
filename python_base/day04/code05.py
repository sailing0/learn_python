"""
    字符串与列表
"""
# 根据某些逻辑，拼接一个字符串．
# result01 = ""
# for item in range(10):
#     result01 += str(item)
# print(result01)

# 每次拼接，创建一个新对象，替换变量地址．
# 变量　=　"0" + "1"
# 变量 = 变量 + "2"

list_result = []
for item in range(10):
    # 没用每次拼接，都生成一个列表．
    list_result.append(str(item))
# join:将列表使用连接符，合成一个字符串
str_result = "+".join(list_result)
print(str_result)

# split:根据分割符拆分字符串
list01 = str_result.split("+")
print(list01)












