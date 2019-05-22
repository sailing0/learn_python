# 练习：将以下代码，不变的部分提取到一个方法find_all中，
#       将变化点，提取到不同方法中．
#       再实现原有功能

# def find_demo02(target):
#     for item in target:
#         if item.cd == 0:
#             yield item
#
# def find_demo03(target):
#     for item in target:
#         if item.atk > 5:
#             yield item
#
# def find_demo04(target):
#     for item in target:
#         if item.atk > 10 and item.costSP == 0:
#             yield item

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

# 不变的
def find_demo04(target,func_condition):
    for item in target:
        # if condition01(item):
        # func_condition 由具体变化点抽象而来
        if func_condition(item):
            yield item

# 变化的
def condition01(item):
    return item.cd == 0

def condition02(item):
    return item.atk > 5

def condition03(item):
    return item.atk > 10 and item.costSP == 0

for item in find_demo04(list_skills,condition01):
    print(item)

