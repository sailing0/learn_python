"""
    列表
    练习:exercise05.py
        exercise06.py
        exercise07.py

"""
# 1. 创建空列表
list01 = []
list01 = list()

# 2. 创建具有默认值的列表 [元素1,元素2....]  list(可迭代对象)
list02 = [1, True, 1.2]
list02 = list("abcd")# ['a', 'b', 'c', 'd']
list02 = list(range(5))

# 3. 添加元素
# append 在末尾追加
list02.append("q")
list02.append("t")
# insert 插入(索引,元素)
list02.insert(1,"x")

# 4. 删除元素
# 移除指定的元素
list02.remove(2)
# 删除指定索引的元素
del list02[1]

# 5. 定位元素(索引  切片)
# 获取前三个元素
# print(list02[:3])
print(list02)
# 修改元素
# list02[:3] = ["a","b","c"]
# list02[:3] = ["a","b","c","d","e"]
# list02[:3] = ["a"]
# del list02[:3]
# print(list02)

# 6. 遍历元素
# 正着
# for i in range(len(list02)):# 0  1  2
#     print(list02[i])
# 跳着
# for i in range(0,len(list02),2):
#     print(list02[i])
# 倒着
for i in range(len(list02) - 1,-1,-1):
    print(list02[i])



