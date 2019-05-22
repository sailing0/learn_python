"""
    可迭代对象：具有__iter__()方法，可以返回迭代器的对象．
"""
list01 = [2,434,5,6,8]

# for item in list01:
#     print(item)

# 面试题：
# 能够被for循环的条件是：可迭代对象（具有__iter__()方法的对象）

# for循环原理
# 1. 获取迭代器对象
# 2. 循环迭代(调用迭代器的__next__方法)
# 3. 捕获StopIteration异常

#1.
# iterator = list01.__iter__()
#2.
# item = iterator.__next__()
# print(item)
#
# item = iterator.__next__()
# print(item)
#
# item = iterator.__next__()
# print(item)
#
# item = iterator.__next__()
# print(item)
#
# item = iterator.__next__() # 最后一次
# print(item)
# 3.
# item = iterator.__next__()# StopIteration
# print(item)

# 1.　获取迭代器对象
iterator = list01.__iter__()
while True:
    try:# 如果获取了全部元素,则执行except
        # 2.　获取下一个元素(迭代过程)
        item = iterator.__next__()
        print(item)
        # 3.停止迭代（StopIteration　错误）
    except StopIteration:
        break # 跳出循环体



