"""
    Encolsing 外部嵌套作用域
"""

# 全局变量G
g01 = 100

def fun01():
    # fun01局部变量Ｌ
    # E外部嵌套作用域
    a = 1

    def fun02():
        b = 2 # fun02局部变量Ｌ
        # print("fun02:", a) # 可以访问外部嵌套变量a
        # a = 2222 # 没有修改外部嵌套变量a，而是创建了新的局部变量a
        # print("fun02:",a)
        nonlocal a # 声明外部嵌套变量a
        a = 2222
        print("fun02:",a)

    fun02()
    print("fun01:",a)

fun01()
