"""
    数据类型

"""

# 1. 整数int
# -- 十进制
num01 = 18
# -- 二进制(每逢2进1)  0   1    10   11   100   101    110  ....
num02 = 0b11
print(num02)
# -- 八进制(每逢8进1) 0 1 ... 7  10   11   12  ...
num03 = 0o10
print(num03)
# -- 十六进制(每逢16进1) 0--9    a(10) -- f(15)
num04 = 0x10
print(num04)

# 小整数对象池
a = 500
b = 500
# id函数:返回变量存储的对象地址
print(id(a))
print(id(b))
# 备注:在交互式中,两个500不是同一个对象.

# 2. 浮点数(小数)float
f01 = 1.0
f02 = 1.234e2
print(f02)
f03 = 1.234e-3
print(f03)

# 3. 字符串str
s01 = "唐僧"
s02 = "10"
s03 = "1.5"

print("10"+"2")
print(10+2)

# 4. 复数 complex
c01 = 1j
c02 = 5 + 1j
print(c02)
print(type(c01))

# 5. 布尔bool
b01 = True # 真的  对的    成立的    满足条件的
b02 = False# 假的  错的    不成立的    不满足条件的
b03 = 1 > 2
print(b03)

# # 6. 数据类型转换
# str_score = input("请输入成绩:")
# # input 函数的结果就是str,如果需要做数学运算,必须转换成数字.
# print(type(str_score))
#
# float_score = float(str_score)
# print(type(float_score))


b04 = bool("False")
print(b04)

i01 = float("5.1") # 如果需要转换的类型,与目标类型不一致,则错误.
print(i01)











