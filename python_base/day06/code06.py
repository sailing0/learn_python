"""
    函数－－返回值（结果）
    返回值：方法定义者　告诉　方法调用者的　结果
    参数：调用者　告诉　定义者
    练习：exercise05/06
"""

# 定义两个整数相加的函数
# def add():
#     # 获取数据
#     number01 = int(input("请输入第一个整数："))
#     number02 = int(input("请输入第二个整数："))
#     # 逻辑处理
#     result = number01 +number02
#     # 显示结果
#     print(result)


def add(number01,number02):
    # 逻辑处理
    result = number01 +number02
    # 返回结果　＋　退出方法
    return result
    # print("当前代码在ｒｅｔｕｒｎ之后，不能执行．")

#　定义变量，接收方法的返回值
re = add(1,2)
print(re)









