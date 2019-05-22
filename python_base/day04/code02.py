'''
    字符串字面值
    练习:exercise02.py
'''

# 单引号与双引号功能相同
str01 = "大家好"
str01 = '大家好'

# 三引号:可见即所得
str01 = '''大
家
好
'''
str01 = """大家好"""

str02 = '我爱"python".'
str02 = "我爱'python'."
print(str02)

# 转义符:改变原始含义的特殊字符
# 如果字符串内部,需要包含多种(单/双/三)引号,使用转义符.
str03 = "我爱\"p'yt\"\"\"hon\""
print(str03)

# \n 换行
str04 = "大家好,\n我是QTX."
print(str04)

# \t 水平制表格 tab 键
str04 = "大家好,\t我是QTX."
print(str04)

str04 = "C:\arogram Files\breative\chareDLL\dADI"
print(str04)

# 格式化字符串
name = "qtx"
age = 32
# 字符串拼接,如果格式复杂,代码可读性比较差.
msg01 = "我的名字是:" + name + ",年龄是:" + str(age) + "."
#
msg02 = "我的名字是:%s,年龄是:%d." % (name, age)
print(msg01)
print(msg02)

# 宽度是5  右对齐
str05 = "整数是:%5d."%(32) #整数是:   32.
# 宽度是5  左对齐
str05 = "整数是:%-5d."%(32) #整数是:32   .
# 宽度是2  不足2位使用0填充
str05 = "时间:%02d."%(2) #时间:02.
# 02:00   01:59    01:09

str05 = "小数:%.2f,"%(1.23556) #小数:1.23.
# round(1.234,2)  是改变数值
num = 1.234
num = round(num,2)
print(str05)




















