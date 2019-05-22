"""
    内存图2.0
    可变对象传参
    练习：exercise01
"""

def fun01(list_target):
    list_target[0] = 2
    print("list_target[0]:" + str(list_target[0]))


list_number = [1,2]
fun01(list_number)
print("list_number:" + str(list_number[0]))





