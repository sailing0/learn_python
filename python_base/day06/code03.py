"""
    for  for 嵌套
"""

"""
    *****
    *****
    *****
"""

# for r in range(3):#      0        1        2
#     for c in range(5):#01234    01234    01234
#         print("*",end = "") # 在一行输出
#     print() # 换行

"""  ４行６列
    ******
    ######
    ******
    ######
"""
# 结论：外层循环控制行　　　内层循环控制列
# for r in range(4):#  ０　　　　　　１　　　　　　　２　　　　３   　
#     for c in range(6):
#         if r % 2 == 0:
#             print("*", end="")
#         else:
#             print("#", end="")
#     print() # 换行
"""
4行     内层循环索引　　　　
#　　　　0　
##      01
###     012
####    0123
"""
# for r in range(4):#     0     1     2      3
#     for c in range(r+1):# 0    01    012    0123
#         print("#", end="")
#     print()
"""
4行        空格　　　　＃　　
####　　　　　　　　　  0123
 ###　      0         012
  ##　      01        01
   #　      012       0　　
"""
# for r in range(4):#       0      1       2       3
#     for c in range(r):#          0       01      012
#         print(" ", end="")
#     for c in range(4-r):# 0123   012
#         print("#", end="")
#     print()
"""
    列表中是否具有相同元素
    [1,4,7,4,8,0,6]
    
    核心：所有元素间两两比较
    思想：
    取出第一个元素，与后面(1,2,3....)进行比较．
    取出第二个元素，与后面(2,3....)进行比较．
    取出第三个元素，与后面(3....)进行比较．
    　　．．．．
"""

list01 = [1, 4, 7, 4, 8, 0, 6]

# if list01[0]  == list01[1]:
#     print("具有相同元素")
#
# if list01[0]  == list01[2]:
#     print("具有相同元素")
#
# if list01[0]  == list01[3]:
#     print("具有相同元素")

# # 取出第一个元素，与后面(1,2,3....)进行比较．
# for c in range(1,len(list01)):
#     if list01[0]  == list01[c]:
#         print("具有相同元素")
#
# # 取出第二个元素，与后面(2,3....)进行比较．
# for c in range(2,len(list01)):
#     if list01[1]  == list01[c]:
#         print("具有相同元素")
#
# # 取出第三个元素，与后面(3....)进行比较．
# for c in range(3,len(list01)):
#     if list01[2]  == list01[c]:
#         print("具有相同元素")

state = False  # 假设没有相同元素
# 取出前几个元素
for r in range(len(list01) - 1):
    # 与后面元素进行比较
    for c in range(r + 1, len(list01)):
        # 如果发现相同元素
        if list01[r] == list01[c]:
            state = True
            break  # 只能退出就近(内)循环体
    if state:
        break  # 退出外层循环
if state:
    print("具有相同元素")
else:
    print("没有相同元素")

# 对列表进行排序：　　[1,4,7,4,8,0,6]
# 核心：两两元素进行比较
#     发现更大的或者更小的则交换
#        降序　　　　　升序

for r in range(len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] > list01[c]:
            # 交换
            list01[r], list01[c] = list01[c], list01[r]

print(list01)

