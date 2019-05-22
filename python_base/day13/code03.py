"""
    模块属性
    # 练习: 将学生管理系统拆分为四个模块
    # XXXModel  ---> model 模型层
    # XXXView --->  ui  表示层
    # XXXController ---> bll   业务逻辑层
    # 调用代码  --->  main  程序入口
"""
from module01 import *

fun01()
# fun04()

# 获取模块文档注释
import module01
print(module01.__doc__)

# 获取模块文件路径
print(module01.__file__)

# 获取模块名称
print(module01.__name__) #模块名  __main__


















