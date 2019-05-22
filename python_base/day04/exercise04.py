#练习:在控制台中输入一个整数,根据整数打印一个矩形
"""  4
    ****
    *  *
    *  *
    ****
"""
number = int(input("请输入:"))
# 头
print("*" * number)
# 中间
for i in range(number -2):
    print("*" + " "*(number - 2) +"*")
# 尾
print("*" * number)