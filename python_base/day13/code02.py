"""
    模块调用
    调用module01.py的成员

    练习:下载double_list_helper.py模块
        新建exercise01.py模块,以3种方式,测试工具类中的方法.
        15:36
"""

# 导入方式1:
# 导入 模块名称
# 本质:将该模块作用域 赋值给 变量 module01
import module01
module01.fun01()
c01 = module01.MyClass01()
c01.fun02()
module01._fun03()

# 导入方式2:
# 本质:将该模块指定成员 赋值给 变量 fun01,MyClass01
# from module01 import fun01,MyClass01,_fun03
# fun01()
# c01 = MyClass01()
# c01.fun02()
# _fun03()

# 导入方式3:
# from module01 import *
#
# fun01()
# c01 = MyClass01()
# c01.fun02()
# _fun03()




