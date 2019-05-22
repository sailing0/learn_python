from day16.common.custom_list_tools import ListHelper


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
# 作业１：
# 解决的问题１：
# 　　　获取敌人列表中，攻击力最小的敌人．
result = ListHelper.get_min(list_skills,lambda e:e.atk)
print(result.name)

result = min(list_skills,key = lambda e:e.atk)
print(result.name)

# 解决的问题２：
# 　　　根据ｃｄ对技能列表进行降叙排列
# 　　　使用内置高阶函数和ListHelper实现．
# ListHelper.order_by_descending(list_skills,lambda e:e.cd)
# for item in list_skills:
#     print(item.cd)

# for item in sorted(list_skills,key = lambda e:e.cd,reverse=True):
#     print(item.cd)

# 如果使用sorted排序，希望修改原有列表，则使用下列代码．
list_skills[:] = sorted(list_skills,key = lambda e:e.cd,reverse=True)
for item in list_skills:
    print(item.cd)

# 面试：自定义排序方法，实现对列表的升序排列．
# 在ListHelper中，定义万能(任意条件／升序／降序)排序方法．
# def sort01(target):
#     for r in range(len(target) - 1):
#         for c in range(r + 1, len(target)):
#             if target[r] > target[c]:
#                 target[r], target[c] = target[c], target[r]

# list01 = [2,6,4,4,5,7]
# sort01(list01)
# for item in list01:
#     print(item)

# def sort02(target):
#     for r in range(len(target) - 1):
#         for c in range(r + 1, len(target)):
#             if target[r] < target[c]:
#                 target[r], target[c] = target[c], target[r]
#
# def sort03(target):
#     for r in range(len(target) - 1):
#         for c in range(r + 1, len(target)):
#             # if target[r].atk < target[c].atk:
#             if xxx(target[r],target[c])
#                 target[r], target[c] = target[c], target[r]

# def xxx(item01,item02):
#     return item01.atk < item02.atk

def sort(target,func_condition):
    """
        万能排序  10:40上课
    :param target: 需要排序的数据
    :param func_condition: 排序的逻辑
          func_condition 类型是函数
                         参数是列表中两个元素
                         返回值是比较的结果
                         方法提是比较的条件
    :return:
    """
    for r in range(len(target) - 1):
        for c in range(r + 1, len(target)):
            if func_condition(target[r],target[c]):
                target[r], target[c] = target[c], target[r]


list01 = [3,34,5,6,8]
sort(list01,lambda e1,e2:e1 < e2)
print(list01)









