# 练习：lambda实现对技能列表的查找　16:17

class SkillData:
    def __init__(self, id, name, cd, atk, costSP):
        self.id = id
        self.name = name
        self.cd = cd
        self.atk = atk
        self.costSP = costSP


list_skills = [
    SkillData(101, "降龙十八掌", 60, 10, 5),
    SkillData(102, "如来神掌", 50, 15, 0),
    SkillData(103, "六脉神剑", 0, 20, 8),
    SkillData(104, "一阳指", 0, 50, 15),
    SkillData(105, "冷酷追击", 15, 30, 9),
]

# 变化的
# def condition01(item):
#     return item.cd == 0
#
# def condition02(item):
#     return item.atk > 5
#
# def condition03(item):
#     return item.atk > 10 and item.costSP == 0

# 通过模块调用
from common.custom_list_tools import ListHelper

for item in ListHelper.find_all(list_skills, lambda item: item.cd == 0):
    print(item)

for item in ListHelper.find_all(list_skills, lambda item: item.atk > 5):
    print(item)

# 练习：16：30
# 解决的问题：
#  查找编号是101的(单个)技能对象
#  查找名称是"降龙十八掌"的(单个)技能对象
#  查找cd大于10的(单个)技能对象

# 解决的步骤：
# 1. 逐个解决问题
# 2. 将共性提取到ListHelper中
# 3. 将变化用lambda表示.

# def find_demo01(target):
#     for item in target:
#         if item.id == 101:
#             return item
#
#
# def find_demo02(target):
#     for item in target:
#         if item.name == "降龙十八掌":
#             return item
#
#
# def find_demo03(target):
#     for item in target:
#         if item.cd > 10:
#             return item

item = ListHelper.first(list_skills, lambda item: item.id == 101)
print(item.name)

# 练习：
# 解决的问题：筛选对象 select
#  技能列表　-->  编号列表
#  技能列表　-->  名称列表
# list_skills = [
#     SkillData(101, "降龙十八掌", 60, 10, 5),
#     SkillData(102, "如来神掌", 50, 15, 0),
#     SkillData(103, "六脉神剑", 0, 20, 8),
#     SkillData(104, "一阳指", 0, 50, 15),
#     SkillData(105, "冷酷追击", 15, 30, 9),
# ]
# list01 = [101,102,103,104,105]

# 17:15
# def find_demo01(target):
#     for item in target:
#         yield item.id
#         yield xxx(item)
#
# def find_demo02(target):
#     for item in target:
#         yield item.name

# def xxx(item):
#     return item.id


for item in ListHelper.select(list_skills, lambda item: item.name):
    print(item)


# 练习：17:29
# 解决的问题：求和 sum
#  技能列表　-->  所有技能编号的和
#  技能列表　-->  所有技能cd的和

# list_skills = [
#     SkillData(101, "降龙十八掌", 60, 10, 5),
#     SkillData(102, "如来神掌", 50, 15, 0),
#     SkillData(103, "六脉神剑", 0, 20, 8),
#     SkillData(104, "一阳指", 0, 50, 15),
#     SkillData(105, "冷酷追击", 15, 30, 9),
# ]

def demo01(target):
    sum_value = 0
    for item in target:
        # sum_value += item.id
        sum_value += xxx(item)
    return sum_value

def demo02(target):
    sum_value = 0
    for item in target:
        sum_value += item.cd
    return sum_value

def xxx(item):
    return item.id


item = ListHelper.sum(list_skills, lambda item: item.cd)
print(item)