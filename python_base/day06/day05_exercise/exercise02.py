"""
　猜拳
  规则：系统随机出拳，在控制台中循环猜测．
  提示：(1)将胜利的策略存入容器
              (
                  ("石头","剪刀"),
                  ("剪刀","布"),
                  ("布","石头")
              )
       (2) 将用户猜的拳与系统出拳形成一个元组
"""

import random


# 胜利策略
wins = (
    ("石头", "剪刀"),
    ("剪刀", "布"),
    ("布", "石头")
)
# 将用户猜的拳与系统出拳形成一个元组        10:42 上课
user_input_index = int(input("请输入整数(0表示石头，１表示剪刀，２表示布)："))
items = ("石头","剪刀","布")
user_input_item = items[user_input_index]

sys_input_index = random.randint(0,2)
sys_input_item = items[sys_input_index]

# 逻辑处理
if user_input_item == sys_input_item:
    print("平局")
elif (user_input_item,sys_input_item) in wins:
    print("赢啦")
else:
    print("输啦")

# 作业：实现三局两胜．











