"""
    函数式编程　－－　方法作为参数
    练习：ｅｘｅｒｃｉｓｅ０３　０４
"""

def fun01():
    print("fun01执行喽")

# 调用fun01，将返回值赋值给变量ａ
# a = fun01()

# 将函数值赋值给变量ａ（没有执行fun01）
a = fun01
# 调用变量ａ，间接执行函数fun01
a()

# 将方法fun01作为方法的参数func进行传递
def fun02(func):
    print("fun02执行喽")
    # 对于fun02的定义者而言，不知道也不需要知道func的具体逻辑．
    func()

fun02(fun01)



list01 = [1,2,33,4,45,6]
# def find_demo01(target):
#     for item in target:
#         if item> 5:
#             yield item
#
# def find_demo02(target):
#     for item in target:
#         if item % 2 != 0:
#             yield item
#
# def find_demo03(target):
#     for item in target:
#         if item < 3:
#             yield item

# --------------------------------------------
# 相同点：
def find_demo(target,func):
    for item in target:
        # 本行代码，又将不变的与变化的紧密相连
        # if condition01(item):
        # 本行代码，使用形参func将不变的与变化的隔离开．
        if func(item):
            yield item
# --------------------------------------------
# 提取不同点：
def condition01(item):
    return item> 5

def condition02(item):
    return item % 2 != 0

def condition03(item):
    return item < 3

for item in find_demo(list01,condition03):
    print(item)









