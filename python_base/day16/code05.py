"""
    lambda 表达式(匿名方法)
    语法：　
    lambda　参数:方法体
    练习：
    exercise05.py
"""


def fun01():
    print("我是普通方法")


fun01()



def fun02(a):
    print("我是普通方法,参数是,", a)


fun02(500)


def fun03():
    return True


print(fun03())

# -------------------------
a01 = lambda: print("我是lambda方法")
a01()

a02 = lambda a: print("我是lambda方法,参数是,", a)
a02(500)

a03 = lambda: True
print(a03())
#------------------------------------

from common.custom_list_tools import ListHelper
list01 = [1,2,33,4,45,6]

for item in ListHelper.find_all(list01,lambda item:item > 5):
    print(item)

for item in ListHelper.find_all(list01,lambda item:item % 2 != 0):
    print(item)

# 提取不同点：
# def condition01(item):
#     return item> 5
#
# def condition02(item):
#     return item % 2 != 0
#
# def condition03(item):
#     return item < 3

# for item in ListHelper.find_all(list01,condition01):
#     print(item)

