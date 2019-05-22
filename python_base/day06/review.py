"""
    day05　复习
    容器
        字符串：字符　不可变　　序列　　
        列表：变量　　可变     序列
        元组：变量　　不可变　　序列
        字典：键值对　可变　　　映射
        集合／固定集合
"""
# 列表
list01 = [1, 2]
list01.append(3)
list01.remove(1)
del list01[1:]
for item in list01:
    print(item)
for item in range(0, len(list01), 2):
    print(item)

# 元组
t01 = (1,2,3)
for i in range(len(t01)-1,-1,-1):
    print(t01[i])

# 字典
d01 = {"a":"A"}
# 第一次存储
d01[1.1] = "b"
# 第二次修改
d01[1.1] = "c"

print(d01["a"])
# 查找不存在的ｋｅｙ，会错误．
# print(d01["b"])
# 建议：不确定是否存在键，则查找前先判断．
if "b" in d01:
    print(d01["b"])

print(d01)

del d01["a"]

# 遍历字典，得到的是ｋｅｙ
for key in d01:
    print(key)

# 遍历字典所有项，得到的是ｋｅｙ，ｖａｌｕｅ
for key,value in d01.items():
    print(key)
    print(value)











