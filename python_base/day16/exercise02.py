# １．创建技能类(编号，技能名称，冷却时间，攻击力，消耗法力)
# 　　创建技能列表．　
# 　　－－　定义函数：查找冷却时间为０的所有技能对象
# 　　－－　定义函数：查找攻击力大于５的所有技能对象
# 　　－－　定义函数：查找攻击力大于１０，并且不需要消耗法力的所有技能．
#   使用列表推导式，与生成器表达式完成
#   通过断点调试，审查程序执行过程，体会两项技术的差异．
#   11:47

class SkillData:
    def __init__(self, id, name, cd, atk, costSP):
        self.id = id
        self.name = name
        self.cd = cd
        self.atk = atk
        self.costSP = costSP

    def __str__(self):
        return self.name

list_skills = [
    SkillData(101, "降龙十八掌", 60, 10, 5),
    SkillData(102, "如来神掌", 50, 15, 0),
    SkillData(103, "六脉神剑", 0, 20, 8),
    SkillData(104, "一阳指", 0, 50, 15),
    SkillData(105, "冷酷追击", 15, 30, 9),
]


# def find_demo02(target):
#     for item in target:
#         if item.cd == 0:
#             yield item

result01 = (item for item in list_skills if item.cd == 0)
result02 = [item for item in list_skills if item.cd == 0]

for item in result01:
    print(item)

for item in result02:
    print(item)

# def find_demo03(target):
#     for item in target:
#         if item.atk > 5:
#             yield item

result01 = (item for item in list_skills if item.atk > 5)
result02 = [item for item in list_skills if item.atk > 5]

for item in result01:
    print(item)

for item in result02:
    print(item)

# def find_demo04(target):
#     for item in target:
#         if item.atk > 10 and item.costSP == 0:
#             yield item
result01 = (item for item in list_skills if item.atk > 10 and item.costSP == 0)
result02 = [item for item in list_skills if item.atk > 10 and item.costSP == 0]

for item in result01:
    print(item)

for item in result02:
    print(item)