"""
    集合
    练习：exercise01
"""
# 1. 创建空集合
s01 = set()
# 2. 创建具有默认值的集合
s01 = {1,2,3,4}
# print(type(s01))
# 3. 其他容器　－－＞　　集合
s02 = set("abcdace")
s02 = set([1,7,56,8,7,8])
#    集合 －－＞　其他容器　　
l02 = list(s02)
t02 = tuple(s02)
# 4. 添加
s02.add("a")
s02.add("b")
s02.add("c")
print(s02)# {1, 7, 8, 'c', 'b', 56, 'a'}

# 5. 删除
# s02.remove(7)
# s02.remove(9) # 如果该元素不存在，则错误．

# if 9 in s02:
#     s02.remove(9)

s02.discard("a") # 如果该元素不存在，不会错误．
print(s02)

# 6. 获取所有元素
for item in s02:
    print(item)

# 7. 计算
s03 = {1,2,3}
s04 = {2,3,4}

# 交集
s05 = s03 & s04
print(s05)# {1, 2}

# 并集
s05 = s03 | s04
print(s05) # {1, 2, 3, 4}

# 补集
s05 = s03 ^ s04
print(s05) # {1, 4}

s05 = s03 - s04
print(s05) #  {1}

s05 = s04 - s03
print(s05) #  {4}

# 子集  超集
s06 = {1,2,3}
s07 = {1,2}
re = s07 <  s06  # True  说明s07 是　　s06 的子集
re = s06 >  s07  # True  说明s06 是　　s07 的超集
print(re)

# 相同　　不同
s08 = {1,2,3}
s09 = {1,2,3}
re = s08 != s09  # True 说明s08 与　　s09 相同
print(re)











