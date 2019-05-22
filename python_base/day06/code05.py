"""
    函数
    函数定义者：做功能的人
    函数调用者：使用功能的人
    练习：exercise03
"""

# 定义函数
def attack():
    print("摆拳")
    print("直拳")
    print("重拳")
    print("....")

# 调用函数
# attack()

# 形式上的参数
def attack_repeat(count):
    for i in range(count):
        print("摆拳")
        print("直拳")
        print("重拳")
        print("....")

#　实际参数
attack_repeat(2)






