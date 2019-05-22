"""
    创建技能类(技能名称，冷却时间，持续时间，攻击距离......)
    要求：使用属性封装变量
   创建技能列表(技能对象的列表)
   -- 查找名称是"降龙十八掌"的技能对象
   -- 查找名称是持续时间大于１０秒的的所有技能对象
   -- 查找攻击距离最远的技能对象
   -- 按照持续时间，对列表升序排列．
"""


class SkillData:
    def __init__(self, name, cd, time, distance):
        self.name = name
        self.cd = cd
        self.time = time
        self.atk_distance = distance

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, value):
        self.__cd = value

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value

    @property
    def atk_distance(self):
        return self.__atk_distance

    @atk_distance.setter
    def atk_distance(self, value):
        self.__atk_distance = value

    def print_self(self):
        print(self.name, self.cd, self.time, self.atk_distance)


list_skills = [
    SkillData("降龙十八掌", 60, 10, 5),
    SkillData("如来神掌", 50, 5, 15),
    SkillData("六脉神剑", 80, 20, 8),
    SkillData("一阳指", 20, 50, 15),
    SkillData("冷酷追击", 15, 30, 9),
]

# -- 查找名称是"降龙十八掌"的技能对象
for item in list_skills:
    if item.name == "降龙十八掌":
        item.print_self()

# -- 查找名称是持续时间大于１０秒的的所有技能对象
result = []
for item in list_skills:
    if item.time > 10:
        result.append(item)

# -- 查找攻击距离最远的技能对象
result = list_skills[0]
for i in range(1, len(list_skills)):
    # 后面的技能对象
    if result.atk_distance < list_skills[i].atk_distance:
        result = list_skills[i]
        # result.atk_distance = list_skills[i].atk_distance

result.print_self()

# -- 按照持续时间，对列表升序排列．
for r in range(len(list_skills) - 1):
    for c in range(r + 1, len(list_skills)):
        if list_skills[r].time  >  list_skills[c].time:
            list_skills[r],list_skills[c] =  list_skills[c],list_skills[r]


# 请用调试,查看列表的取值.
print(list_skills)











