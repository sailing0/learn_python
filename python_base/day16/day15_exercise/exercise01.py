# １．创建技能类(编号，技能名称，冷却时间，攻击力，消耗法力)
# 　　创建技能列表．
# 　　－－　定义函数：查找编号是１０１的技能对象
# 　　－－　定义函数：查找冷却时间为０的所有技能对象
# 　　－－　定义函数：查找攻击力大于５的所有技能对象
# 　　－－　定义函数：查找攻击力大于１０，并且不需要消耗法力的所有技能．

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


# 因为需要查找的结果只有一个，所以使用return返回数据．
# 比使用yield返回数据，在调用者看来，更加方便吧．
def find_demo01(target):
    for item in target:
        if item.id == 101:
            return item

s01 = find_demo01(list_skills)
print(s01.id)


def find_demo02(target):
    for item in target:
        if item.cd == 0:
            yield item

result = find_demo02(list_skills)
# 不能获取指定结果
# 因为：此时生成器函数并没有计算处结果．
# print(result[1].name)
# for item in result:
#     print(item.name)


result = find_demo02(list_skills)
# 通过生成器创建列表
# 由惰性查找(优势：节省内存)　转换为　立即查找(优势：灵活获取结果)
result = list(result)
# print(result[1].name)


def find_demo03(target):
    for item in target:
        if item.atk > 5:
            yield item

# 调用生成器函数，创建迭代器对象
result = find_demo03(list_skills)
for item in result:# __next__()
    print(item.name)

print("---------------")
# 如果没有下一行代码，再次for使用过的生成器对象，不会再有结果．
# result = find_demo03(list_skills)
for item in result:
    print(item.name)

# for item in find_demo03(list_skills):
    # ....


def find_demo04(target):
    for item in target:
        if item.atk > 10 and item.costSP == 0:
            yield item

for item in find_demo04(list_skills):
    print(item.name)


