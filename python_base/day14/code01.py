"""
    包(文件夹)
    # 练习1: 目标 -- 在实际项目结构中,随心所欲的调用不同模块成员.
    # 1. 根据目录结构,创建相应的包与模块.
    # 2. 在相应模块中,定义函数/类.
    # 3. 在main中,调用skill_manager模块中成员
    # 4. 在skill_manager模块中调用skill_deployer模块成员
    # 5. 在skill_data模块中,调用list_helper模块成员.

    练习2:创建如下结构:
    project
        package01
            -- m01.py
            -- exercise01.py
        main.py
    在exercise01.py 中调用m01模块的成员.
    测试:在main中开始运行
         在exercise01中开始运行
    要求:使用终端
    14:50
"""


# python程序结构
# 包
#     模块
#         类
#             函数()/方法()
#                 语句


# # 方式1:import 包.模块
# import package01.module01
# # 使用:包.模块.成员
# package01.module01.fun01()


# # 方式2:from 包 import 模块
# from package01 import module01
# # 使用:模块.成员
# module01.fun01()

# # 方式3:
# from package01 import *
# # 在包的__init__文件中,定义__all__ 属性
# module01.fun01()


# [推荐]
# from 包.模块 import 成员
from package01.module01 import *
fun01()






