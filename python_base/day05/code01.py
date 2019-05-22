"""
    画出下列代码内存图
"""

list01 = [1,2]
# 将列表地址赋值给list02
list02 = list01
# 改变的是列表的第一个元素
list01[0] = 100
print(list02[0])# １００


list01 = [1,2]
# 将列表地址赋值给list02
list02 = list01
# 改变的是列表的第一个元素
list01 = [100]
print(list02[0])# １


list01 = [1,2]
# 将列表中元素复制一份
# list02 = list01[:]
# 将列表中元素复制一份
list02 = list01.copy()
list01[0] = 100
print(list02[0])# １

list01 = [1,[2,3]]
# 将列表中元素复制一份(只拷贝１层)
list02 = list01.copy() # 浅拷贝
list01[1][0] = 200
print(list02[1][0]) # ?200


import copy
list01 = [1,[2,3]]
# 将列表中元素复制一份(只拷贝１层)
# list02 = list01.深拷贝()
list02 = copy.deepcopy(list01) # 深拷贝
list01[1][0] = 200
print(list02[1][0]) # ?2

















