"""
    __slots__ 属性
"""
class SkillData:
    # 限制当前类,创建的对象,只能具有的实例变量.
    __slots__ = ("__name")

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


s01 = SkillData("技能名称")
# s01.name = "降龙十八掌"
print(s01.name)
# 为当前对象,添加实例变量
# s01.time = 5
# print(s01.time)
# print(s01.__dict__) # 因为使用了__slots__属性,所以不是使用__dict__.
