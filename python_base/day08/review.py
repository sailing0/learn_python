"""
    day08 复习
    
"""
# 1. 函数内存图
def fun01(p1, p2):
    p1 = 2
    p2 = [2]  # 修改的是栈空间的变量
    # p2[0] = 2 #修改的是传入的对象


num = 1
list01 = [1]

fun01(num, list01)
print(num, list01)  # ?1  2

g01 = 1
g_list = [1]

# 作用域
def fun02():
    print(g01)

    # 没有修改变量g_list，修改的是指向的列表对象，所以不用global.
    g_list[0] = 2
    # 修改全局变量，必须使用global关键字声明．
    # global g01
    # g01 = 2


fun02()
print(g_list)  # [2]


# 3, 参数
"""
实参：
    -- 位置实参：fun03(1,2,3)
        -- 序列实参：
        # 运行时，根据某些逻辑计算而来．
          list01 = [1,2,3]
        　fun03(*list01)
        
    -- 关键字实参：fun03(b = 1,c = 2)
        -- 字典实参：
        # 运行时，根据某些逻辑计算而来．
        　dict01 = {"b":2,"c":"3"}
        　fun03(**dict01)

形参：
    -- 默认形参
        def fun03(a = 0,b = 0,c=0):
            pass
    -- 位置形参
         def fun03(a,b,c):
                pass
         -- 星号元组形参　def fun03(*args)
         
    -- 关键字形参
        def fun03(*args,a,b,c):
            pass
            
        -- 双星号字典形参
            def fun03(**kwargs)
"""














