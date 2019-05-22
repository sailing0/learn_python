"""
目标１：熟练运用ListHelper.
准备：
　　－－　创建敌人类（编号／姓名／攻击力／血量／攻击速度．．．）
　　－－　创建敌人列表
练习：
　　 1. 查找所有死人.
    2. 查找编号是101的敌人
    3. 查找所有活人.
    4. 计算所有敌人攻击力总和
    5. 查找所有攻击速度在５－－１０之间的敌人
    6. 查找所有敌人的姓名

目标２：可以在实际项目中，灵活运用函数式编程思想．
解决的问题：获取满足条件的最后一个对象
    获取最后一个活人
    获取攻击速度大于５的最后一个敌人

解决的问题：获取满足条件的对象总数
    获取具有生命值的对象总数
    获取攻击速度小于２０的敌人总数

解决的问题：判断列表中是否包含某个元素
    获取列表中是否具有死人
    获取列表中是否具有攻击速度大于１０的敌人
"""
from day16.common.custom_list_tools import ListHelper


# 敌人类（编号／姓名／攻击力／血量／攻击速度．．．）
class Enemy:
    def __init__(self, id, name, hp, atk, atk_speed):
        self.id = id
        self.name = name
        self.hp = hp
        self.atk = atk
        self.atk_speed = atk_speed

list01 = [
    Enemy(101,"玄冥大老",200,800,5),
    Enemy(102,"玄冥小老",150,700,3),
    Enemy(103,"qtx",800,1000,50),
    Enemy(104,"吕泽玛利亚",0,300,2),
    Enemy(105,"赵金多",500,900,10),
]

# 　　 1. 查找所有死人.  10:44
for item in ListHelper.find_all(list01,lambda e:e.hp == 0):
    print(item.name)
#     2. 查找编号是101的敌人
result = ListHelper.first(list01,lambda e:e.id == 101)
print(result.name)
#     3. 查找所有活人.
for item in ListHelper.find_all(list01,lambda e:e.hp > 0):
    print(item.name)
#     4. 计算所有敌人攻击力总和
result = ListHelper.sum(list01,lambda e:e.atk)
print(result)
#     5. 查找所有攻击速度在５－－１０之间的敌人
for item in ListHelper.find_all(list01,lambda e: 5 <= e.atk_speed <= 10):
    print(item.name)
#     6. 查找所有敌人的姓名
# for item in ListHelper.select(list01,lambda e:e.name):
#     print(item)

# 结果是生成器对象
result = ListHelper.select(list01,lambda e:e.name)
# 生成器　--> 列表
result = list(result)
for item in result[1:3]:
    print(item)

# 解决的问题：获取满足条件的最后一个对象
#     获取最后一个活人
#     获取攻击速度大于５的最后一个敌人

# def find_demo01():
#     for i in range(len(list01) - 1,-1,-1):
#         if list01[i].hp >0:
#         if xxx(list01[i]):
#             return list01[i]

# def find_demo02():
#     for i in range(len(list01) - 1,-1,-1):
#         if list01[i].atk_speed >5:
#             return list01[i]

# def xxx(item):
#     return item.hp >0

result = ListHelper.last(list01,lambda e:e.atk_speed >5)
print(result.name)


# 解决的问题：获取满足条件的对象总数
#     获取具有生命值的对象总数
#     获取攻击速度小于２０的敌人总数
# def find_demo01(target):
#     count_value = 0
#     for item in target:
#         # if item.hp >0:
#         if xxx(item):
#             count_value += 1
#     return count_value
#
# def xxx(item):
#     return item.hp >0

count = ListHelper.get_count(list01,lambda e:e.atk_speed < 20)
print(count)


# 解决的问题：判断列表中是否包含某个元素
#     获取列表中是否具有死人
#     获取列表中是否具有攻击速度大于１０的敌人
# def demo01(target):
#     for item in target:
#         # if item.hp == 0:
#         if xxx(item):
#             return True
#     return False
#
# def xxx(item):
#     return item.hp == 0

result = ListHelper.exists(list01,lambda e:e.hp == 0)
print(result)


# 练习：
# 解决的问题：删除满足条件的所有对象
# 删除所有死人
# 删除编号是101的敌人
# 删除攻击力小于５的敌人
count = ListHelper.delete_all(list01,lambda e:e.hp == 0)
print(count)


# 练习：14:13
# 解决的问题：获取满足条件的最大值
# 获取血量最大的敌人
# 获取攻击力最强的
# ...

# def demo01(target):
#     max_value = target[0]
#     for i in range(1, len(target)):
#         # if max_value.hp < target[i].hp:
#         if xxx(max_value) < xxx(target[i]):
#             max_value = target[i]
#     return max_value
#
# def xxx(item):
#     return item.hp

max = ListHelper.get_max(list01,lambda e:e.hp)
print(max.name)

# 练习：14:45
# 解决的问题：根据指定条件升序排列列表
# 按照血量升序排列
# 按照攻击力升序排列
# def demo01(target):
#     for r in range(len(target)-1):
#         for c in range(r+1,len(target)):
#             # if target[r].hp > target[c].hp:
#             if xxx(target[r]) > xxx(target[c]):
#                 target[r],target[c] = target[c],target[r]
#
# def demo02(target):
#     for r in range(len(target)-1):
#         for c in range(r+1,len(target)):
#             if target[r].atk > target[c].atk:
#                 target[r],target[c] = target[c],target[r]
#
# def xxx(item):
#     return item.hp

ListHelper.order_by(list01,lambda e:e.hp)
for item in list01:
    print(item.hp)




