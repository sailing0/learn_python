"""
    形参传递方式
        默认形参

        位置形参
            -- 星号元组形参：位置实参数量无限

        命名关键字形参：要求必须使用关键字实参
            -- 双星号字典形参：关键字实参数量无限

    学习目标：会调用其他人写的函数．

    练习：exercise04
"""


# 位置形参
def fun01(a, b, c):
    pass


# 星号元组形参
def fun02(*args):
    # 对于方法内部而言，就是元组
    # 对于调用者而言，可以传递数量无限的位置实参．
    print(args)


# fun02()
# fun02(1)
# fun02(1,2,3,4)

# 命名关键字形参:强制实参使用关键字传递．
# a,b 是命名关键字形参
def fun03(*, a, b):
    print(a)
    print(b)


# b 是命名关键字形参
def fun04(*args, b):
    print(args)
    print(b)


# fun03(a = 1,b = 2)
fun04(3, 44, 3, b =22)


# 双星号字典形参
def fun05(**kwargs):
    # 对于方法内部而言，就是字典，
    # 对于调用者而言，可以传递数量无限的关键字实参．
    print(kwargs)


fun05(a=1, b=2)


# 调用
def fun06(*args, **kwargs):
    print(args)
    print(kwargs)


# 数量无限的位置实参，数量无限的关键字实参
fun06(1, 2, 3, 4, 5, a="a", b=1.5)


def fun07(a, b, *args, c, d, **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)


fun07(1, 2, 3, 4, 5, d="d", c="c")
fun07(1, 2, 3, 4, 5, d="d", c="c", e="ee")
fun07(1, 2, d="d", c="c")

print(1,2,3,4,5) # 1 2 3 4 5
print(1,2,3,4,5,"#") #   1#2#3#4#5






