# 1. 参照下列代码，定义判断是否是奇数的方法．
#     number = int(input("请输入整数:"))
#     if number % 2 == 1:
#         print("奇数")
#     else:
#         print("偶数")

def is_uneven(number):
    # if number % 2 == 1:
    #     return True
    # else:
    #     return False
    #　条件表达式
    # return True if number % 2 == 1 else False
    return number % 2 == 1

re = is_uneven(6)
print(re)





