"""
    字符串操作
    练习:exercise03.py
        exercise04.py
"""
# 1. 数学运算
str01 = "悟空"
str02 = "八戒"
# 创建新对象
str03 = str01 + str02
str01 += str02
# 容器可以与数字相乘
print(str02 * 2)  # "八戒八戒"
str02 *= 2
print(str02)

print("abc" > "adc")

# 2. 成员运算
str03 = "猥琐发育,别浪!"
print("猥琐" in str03)

str04 = "abcde"
print(str04[0])
print(str04[len(str04) - 1])
print(str04[-1])

# 索引不能越界
# print(str04[5])  # IndexError

# 切片
print(str04[0:3])# abc
print(str04[0:3:2]) # ac
print(str04[::]) # abcde
print(str04[::-1]) # edcba
print(str04[-2:-5:-1])# bcd
print(str04[1:1]) # 空
print(str04[1:10]) #bcde  切片即使越界,也不会错误.
print(str04[3:1]) # 空
print(str04[3:1:-1])# dc
print(str04[-2:])# de
print(str04[-2:1])# 空









