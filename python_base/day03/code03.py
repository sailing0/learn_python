"""
    循环语句
        -- for

"""
# for 变量名 in 可迭代对象:
#     语句

# for element in "我爱Python":
#     print(element)

# range()函数:整数生成器
# 熟练正叙  倒叙   跳着 生成数字

# for element in range(1,5,1): # 1  2  3  4
#     print(element)
# range(1,6,2): # 1  3  5
# range(3): #0  1   2
# range(5,-1,-1): #5  4   3  2   1   0
# 结论:for比while,更适合做预定次数的循环.
count = 0
while count < 3:
    print(count)
    count+=1
for i in range(3):
    print(i)


