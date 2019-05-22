"""
    高阶函数

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
    Enemy(101, "玄冥大老", 200, 800, 5),
    Enemy(102, "玄冥小老", 150, 700, 3),
    Enemy(103, "qtx", 800, 1000, 50),
    Enemy(104, "吕泽玛利亚", 0, 300, 2),
    Enemy(105, "赵金多", 500, 900, 10),
]

# 1. filter 过滤，类似于ListHelper.find_all.
# 过滤出编号大于102的敌人
# for item in filter(lambda e: e.id > 102, list01):
#     print(item.id)
#
# for item in ListHelper.find_all(list01, lambda e: e.id > 102):
#     print(item.id)

# 2. map 映射，类似于ListHelper.select
# 映射出所有敌人的姓名
for item in map(lambda e:e.name,list01):
    print(item)

for item in ListHelper.select(list01,lambda e:e.name):
    print(item)

# # 按照血量升序排列,类似于ListHelper.order_by
# for item in sorted(list01,key = lambda e:e.hp ):
#     print(item.hp)
#
# # 按照血量降叙排列
# for item in sorted(list01,key = lambda e:e.hp,reverse=True):
#     print(item.hp)

# ListHelper.order_by(list01,lambda e:e.hp)
# for item in list01:
#     print(item.hp)


# 获取攻击力最大的敌人
result = max(list01,key = lambda e:e.atk)
print(result.name)

result = ListHelper.get_max(list01,lambda e:e.atk)
print(result.name)



